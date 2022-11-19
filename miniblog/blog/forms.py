from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import gettext,gettext_lazy as _

class User_signup(UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {"username":forms.TextInput(attrs={"class":'form-control'}),
        "first_name":forms.TextInput(attrs={"class":'form-control'}),
        'last_name':forms.TextInput(attrs={"class":"form-control"}),
        'email':forms.TextInput(attrs={"class":"form-control"}),
        }
class LoginForm(AuthenticationForm):
        username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control',"autofocus":True}))
        password = forms.CharField(label=_('ptassword'),strip=False,widget=forms.PasswordInput(attrs={"class":"form-control",'autocomplete':"current-password"}))

class PostForm(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ['title','desc']
        labels = {"title":"Enter your title","desc":"Description"}
        widgets = {'title':forms.TextInput(attrs={"class":"form-control"}),"desc":forms.Textarea(attrs={"class":"form-control"})}
        error_messages = {"title":{"required":"Title Field is required"},"desc":{"required":"This Field is required"}}