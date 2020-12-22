from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from Hub.models import User, Movies, Booking

# User Sign Up Form. * If warning showed on Password1 and phone, It is because of the use of regex in it. 
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'FirstName'}),max_length=20, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'LastName'}),max_length=15, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'UserName'}),max_length=30, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Email'}),max_length=254,required=True)
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Passord','pattern':'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}','id':'myInput1' }),max_length=16, required=True)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Confirm Password', 'id':'myInput'}),max_length=16, required=True)
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Phone','pattern':'/(7|8|9)\d{9}/'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','phone')

# Update form for User.
class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','is_admin')

# Update form for Movie.
class Movie_form(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('__all__')

# Movie Creation form
class Create_Movie(forms.ModelForm):
    date_of_start = forms.DateField(widget=forms.DateInput(attrs={'name':'dos','class':'datepicker1','placeholder':'DateOfStart','id':'date_ex'}), required=True)
    date_of_end = forms.DateField(widget=forms.DateInput(attrs={'name':'doe','class':'datepicker2','placeholder':'DateOfEnd','id':'date_ox'}), required=True)
    moviename = forms.CharField(widget= forms.TextInput(attrs={'name':'name','placeholder':'Moviename'}),required=True)
    movie_heading = forms.CharField(widget= forms.TextInput(attrs={'name':'heading','placeholder':'MovieHeading'}),required=True)
    movie_image = forms.ImageField(widget= forms.FileInput(attrs={'name':'poster','placeholder':'Poster'}),required=True)
    movie_review = forms.CharField(widget= forms.TextInput(attrs={'name':'review','placeholder':'Review'}),required=True)
    class Meta:
        model = Movies
        fields = ('__all__')

# Seat Updateing Form
class Booking_Form(forms.ModelForm):
    # All the seats Listed 
    A1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A1', 'type':'checkbox', 'id':'A1'} ),required=False)
    A2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A2', 'type':'checkbox', 'id':'A2'} ),required=False)
    A3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A3', 'type':'checkbox', 'id':'A3'} ),required=False)
    A4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A4', 'type':'checkbox', 'id':'A4'} ),required=False)
    A5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A5', 'type':'checkbox', 'id':'A5'} ),required=False)

    B1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B1', 'type':'checkbox', 'id':'B1'} ),required=False)
    B2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B2', 'type':'checkbox', 'id':'B2'} ),required=False)
    B3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B3', 'type':'checkbox', 'id':'B3'} ),required=False)
    B4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B4', 'type':'checkbox', 'id':'B4'} ),required=False)
    B5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B5', 'type':'checkbox', 'id':'B5'} ),required=False)

    C1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'C1', 'type':'checkbox', 'id':'C1'} ),required=False)
    C2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'C2', 'type':'checkbox', 'id':'C2'} ),required=False)
    C3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'C3', 'type':'checkbox', 'id':'C3'} ),required=False)
    C4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'C4', 'type':'checkbox', 'id':'C4'} ),required=False)
    C5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'C5', 'type':'checkbox', 'id':'C5'} ),required=False)

    D1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'D1', 'type':'checkbox', 'id':'D1'} ),required=False)
    D2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'D2', 'type':'checkbox', 'id':'D2'} ),required=False)
    D3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'D3', 'type':'checkbox', 'id':'D3'} ),required=False)
    D4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'D4', 'type':'checkbox', 'id':'D4'} ),required=False)
    D5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'D5', 'type':'checkbox', 'id':'D5'} ),required=False)

    E1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'E1', 'type':'checkbox', 'id':'E1'} ),required=False)
    E2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'E2', 'type':'checkbox', 'id':'E2'} ),required=False)
    E3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'E3', 'type':'checkbox', 'id':'E3'} ),required=False)
    E4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'E4', 'type':'checkbox', 'id':'E4'} ),required=False)
    E5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'E5', 'type':'checkbox', 'id':'E5'} ),required=False)

    F1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'F1', 'type':'checkbox', 'id':'F1'} ),required=False)
    F2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'F2', 'type':'checkbox', 'id':'F2'} ),required=False)
    F3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'F3', 'type':'checkbox', 'id':'F3'} ),required=False)
    F4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'F4', 'type':'checkbox', 'id':'F4'} ),required=False)
    F5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'F5', 'type':'checkbox', 'id':'F5'} ),required=False)

    G1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'G1', 'type':'checkbox', 'id':'G1'} ),required=False)
    G2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'G2', 'type':'checkbox', 'id':'G2'} ),required=False)
    G3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'G3', 'type':'checkbox', 'id':'G3'} ),required=False)
    G4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'G4', 'type':'checkbox', 'id':'G4'} ),required=False)
    G5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'G5', 'type':'checkbox', 'id':'G5'} ),required=False)

    H1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'H1', 'type':'checkbox', 'id':'H1'} ),required=False)
    H2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'H2', 'type':'checkbox', 'id':'H2'} ),required=False)
    H3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'H3', 'type':'checkbox', 'id':'H3'} ),required=False)
    H4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'H4', 'type':'checkbox', 'id':'H4'} ),required=False)
    H5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'H5', 'type':'checkbox', 'id':'H5'} ),required=False)

    I1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'I1', 'type':'checkbox', 'id':'I1'} ),required=False)
    I2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'I2', 'type':'checkbox', 'id':'I2'} ),required=False)
    I3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'I3', 'type':'checkbox', 'id':'I3'} ),required=False)
    I4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'I4', 'type':'checkbox', 'id':'I4'} ),required=False)
    I5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'I5', 'type':'checkbox', 'id':'I5'} ),required=False)

    class Meta:
        model = Booking
        fields = ('A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5',
        'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2', 'G3', 'G4', 'G5',
        'H1', 'H2', 'H3', 'H4', 'H5', 'I1', 'I2', 'I3', 'I4', 'I5', 'J1', 'J2', 'J3', 'J4', 'J5')