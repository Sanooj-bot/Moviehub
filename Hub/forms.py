from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from Hub.models import User, Movies, Booking

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

class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','is_admin')

class Movie_form(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('__all__')

class Booking_Form(forms.ModelForm):

    A1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A1','class':'cust-checkbox'} ))
    A2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A2','class':'cust-checkbox'} ))
    A3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A3','class':'cust-checkbox'} ))
    A4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A4','class':'cust-checkbox'} ))
    A5 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'A4','class':'cust-checkbox'} ))

    B1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B1','class':'cust-checkbox'} ))
    B2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B2','class':'cust-checkbox'} ))
    B3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B3','class':'cust-checkbox'} ))
    B4 = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'B4','class':'cust-checkbox'} ))
    
    class Meta:
        model = Booking
        fields = ('A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5',
        'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2', 'G3', 'G4', 'G5',
        'H1', 'H2', 'H3', 'H4', 'H5', 'I1', 'I2', 'I3', 'I4', 'I5', 'J1', 'J2', 'J3', 'J4', 'J5')