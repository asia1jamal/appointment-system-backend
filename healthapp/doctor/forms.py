"""from django import forms
from .models import Patient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm"""

"""class SignupForm(UserCreationForm):
    class Meta:
        model=User
        feields=['username','email','password1','password2']"""




"""
class PatientSignUp(forms.ModelForm):
    username=forms.CharField(label='username',max_length=10)
    email=forms.EmailField(label='email')
    FirstName=forms.CharField(label='first name')
    MiddleName=forms.CharField(label='Middle name')
    LastName=forms.CharField(label='Last name')
    password1=forms.CharField(label='password',widget=forms.PasswordInput(),min_length=8)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model=User
        fields=('__all__')
   #عملية التحقق من الباسوورد
    def clean_password2(self):
       cd= self.cleaned_data
       if cd['password1'] != cd['password2']:
        raise forms.ValidationError('passwords are not the same')
       return cd['password2']
    #عملية التحقق من انو مافي يوزرين نفس الاسم
    def cleanUserName(self):
        cd=self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('Exsist username ')
        return cd['username']



class LoginForm(forms.ModelForm):
    username=forms.CharField(label='username',max_length=10)
    password=forms.CharField(label='password',widget=forms.PasswordInput())
    class Meta:
        model =User
        fiellds=('username','password')

class appoinment_form(forms.ModelForm):"""
    