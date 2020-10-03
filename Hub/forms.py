from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from Hub.models import User, Movies

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'FirstName'}),max_length=20, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'LastName'}),max_length=15, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'UserName'}),max_length=30, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Email'}),max_length=254,required=True)
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Passord','pattern':'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'}),max_length=16, required=True)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Confirm Password'}),max_length=16, required=True)
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