# Imports
from Hub.forms import SignUpForm, User_Form, Movie_form, Booking_Form, Create_Movie
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from Hub.decorators import unauthenticated_user, admin_user
from django.contrib.auth import login, authenticate, logout
from Hub.models import User, Movies, Booking, Ticket
from django.views.decorators.csrf import csrf_exempt
from Hub.filters import UserFilter, MovieFilter
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
import threading
import datetime
import urllib
import stripe
import json

# Values/Variables
stripe.api_key = settings.STRIPE_PRIVATE_KEY
val = None
thre = None

# Thread for faster Email senting.
class EmailThreding(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently = False)

# Signup View With Email senting and RecaptchaV2.
@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if form.is_valid():
            if result['success']:
                form.save() 
                email = form.cleaned_data.get('email')
                Email_Subject = "Account has been created successfully"
                Email_Body = "Your account has been registered at MovieHub. Worlds No.1 Movie booking site!"
                email = EmailMessage(
                    Email_Subject,
                    Email_Body,
                    'noreply@moviehubcom',
                    [email]
                )
                EmailThreding(email).start()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Login View with Email notification     
@unauthenticated_user    
def logins(request):
    if request.method == 'POST':
        # Getting data user inserted.
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Verifying the values with database.
        user = authenticate(request, email = email, password = password)
        # If Authentication sucess. 
        if user is not None:
            login(request, user) # Logins
            # Stating the process for email.
            Email_Subject = "There is a new login in your Account"
            Email_Body = "You have loged in to MovieHub. Worlds No.1 Movie booking site!"
            email = EmailMessage(
                Email_Subject,
                Email_Body,
                'noreply@moviehubcom',
                [email]
            )
            EmailThreding(email).start()
            return redirect('home')
        # Else Show message Error.
        else:
            messages.info(request, 'Email or Password incorrect')

    context = {}
    return render(request, 'login.html' , context)

# Home page View
def home(request):
    context = {}
    context["images"] = Movies.objects.all()
    return render(request, 'home.html', context)

# Log Out View
def logout_view(request):
    logout(request)
    return redirect('login')

# Seperate Movie Details
def movie_detail(request, id):
    data = Movies.objects.get( id = id )
    if request.method == "POST":
        date = request.POST.get( 'date' )
        movie = data.moviename
        se = Booking.objects.get(Movie_Name = movie, Date_Of_Show = date)
        return redirect('seat', pk = se.id)
    context = {'data':data}
    return render(request, "MovieDetail.html", context)

# User List View
@admin_user
def user_list(request):
    user = User.objects.all()
    userfilter = UserFilter(request.GET, queryset=user)
    user = userfilter.qs
    context = {'user' : user, 'userfilter' : userfilter}
    return render(request, 'UserList.html', context)

# Movie List View
@admin_user
def MovieView(request):
    movie = Movies.objects.all()
    moviefilter = MovieFilter(request.GET, queryset=movie)
    movie = moviefilter.qs
    context = {'movie' : movie,'moviefilter' : moviefilter}
    return render(request, 'MovieList.html', context)

# User Update View
@admin_user
def user_update(request, pk):
    data = User.objects.get(id = pk)
    form = User_Form(instance = data)
    if request.method == 'POST':
        form = User_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('userlist')
    context ={'form' : form} 
    return render(request, "UserUpdate.html", context)

# Movie Update View
@admin_user    
def movie_update(request, pk):
    data = Movies.objects.get(id = pk)
    form = Movie_form(instance = data)
    if request.method == 'POST':
        form = Movie_form(request.POST, instance = data)
        if form.is_valid():
            form.save()
            return redirect('movielist')
    context ={'form' : form} 
    return render(request, "MovieUpdate.html", context)  
    
# Payment Succcess Page
def thanks(request):
    s = thre()
    if s: 
        return render(request, 'thanks.html')
    
# Stripe Checkout
@csrf_exempt
def checkout(request):
    qty = val()
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HYqj9DhYPfk6E3241lev41V',
            'quantity': qty,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })

# Payment Failed Page
def failed(request):
    return render(request, 'failed.html')

# Movie Delete View
@admin_user
def movie_delete(request, pk):
    data = Movies.objects.get(id = pk)
    if request.method =="POST":
        data.delete() 
        return redirect("movielist")
    context ={}  
    return render(request, "MovieDelete.html", context)

# User Delete View
@admin_user
def user_delete(request, pk):
    data = User.objects.get(id = pk)
    if request.method == "POST":
        data.delete() 
        return HttpResponseRedirect("userlist")
    context ={}  
    return render(request, "UserDelete.html", context)

# Selectin Seat View
@csrf_exempt
def seat_select(request,pk):
    data = Booking.objects.get(id = pk)
    form = Booking_Form(instance = data)
    if request.method == 'POST':
        form = Booking_Form(request.POST, instance=data)
        name = request.POST.get('name')
        number = request.POST.get('number')
        seats = request.POST.get('seats')
        global val
        def val():
            return number
        
        if form.is_valid():
            global thre
            # Saving after Payment Sucess only.
            def thre():
                form.save()
                p = Ticket.objects.create(Name = name, Number = number, Seats = seats)
                return True
            return redirect('pay')
    context ={'form':form, } 
    return render(request, "seat.html", context)

# Create Movie page
def create_movie(request):
    form = Create_Movie()
    
    if request.method == 'POST':
        form = Create_Movie(request.POST, files=request.FILES)
        
        if form.is_valid(): 
            DOS = form.cleaned_data['date_of_start']
            DOE = form.cleaned_data['date_of_end']
            name = form.cleaned_data['moviename']
            show = DOE - DOS
            shows = show.days
            for i in range(shows):
                DOS += datetime.timedelta(days = 1)
                p = Booking.objects.create(Movie_Name = name, Date_Of_Show = DOS) # Creating Seats for each day.
            form.save()
            return redirect('movielist')
    else:
        context ={'form':form}
        return render(request, "create_movie.html", context)  

# Confirm Pay and Showing Instruction page.
def pay(request):
    return render(request, 'pay.html')
    
    
    
    
    
    
    
    
    
        
        
        

          
    

