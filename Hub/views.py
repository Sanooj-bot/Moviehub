import json
import urllib
import threading
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Hub.forms import SignUpForm, User_Form, Movie_form
from Hub.models import User, Movies
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import DetailView
from Hub.decorators import unauthenticated_user, admin_user
from Hub.filters import UserFilter, MovieFilter

class EmailThreding(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)
@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
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
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
@unauthenticated_user    
def logins(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email = email,password = password)

        if user is not None:
            login(request, user)
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
        else:
            messages.info(request,'Email or Password incorrect')

    context = {}
    return render(request, 'login.html' , context)
def home(request):
    context = {}
    context["images"] = Movies.objects.all()
    return render(request, 'home.html', context)
def logout_view(request):
    logout(request)
    return redirect('login')    

def movie_detail(request, id):
    context = {}
    context["data"] = Movies.objects.get( id = id )
    return render(request, "MovieDetail.html", context)

@admin_user
def user_list(request):
    user = User.objects.all()
    userfilter = UserFilter(request.GET, queryset=user)
    user = userfilter.qs
    context = {'user':user, 'userfilter':userfilter}
    return render(request,'UserList.html',context)
@admin_user
def MovieView(request):
    movie = Movies.objects.all()
    moviefilter = MovieFilter(request.GET, queryset=movie)
    movie = moviefilter.qs
    context = {'movie':movie,'moviefilter':moviefilter}
    return render(request,'MovieList.html',context)
@admin_user
def user_update(request, pk):
    data = User.objects.get(id = pk)
    form = User_Form(instance = data)
    if request.method == 'POST':
        form = User_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('userlist')
    context ={'form':form} 
    return render(request, "UserUpdate.html", context)
@admin_user    
def movie_update(request, pk):
    data = Movies.objects.get(id = pk)
    form = Movie_form(instance = data)
    if request.method == 'POST':
        form = Movie_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('movielist')
    context ={'form':form} 
    return render(request, "MovieUpdate.html", context)  
    

