from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages
from .models import blogPost
from django.contrib.auth.models import Group
from .forms import *
# Create your views here.
# home
def home(request):
    posts = blogPost.objects.all()
    return render(request,'blog/home.html',{"posts":posts})

# about
def about(request):
    return render(request,'blog/about.html')

# contact
def contact(request):
    return render(request,'blog/contact.html')

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = blogPost.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dashboard.html',{"posts":posts,"full_name":full_name,'gps':gps})
    else:
        return HttpResponseRedirect('/login/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# signup
def Signup(request):
    if request.method == "POST":
        fm = User_signup(request.POST)
        if fm.is_valid():
            messages.success(request,'Contratulation! You become an author')
            user=fm.save()
            group = Group.objects.get(name="Author") 
            user.groups.add(group)        
    else:
        fm = User_signup()
    return render(request,'blog/signup.html',{"forms":fm})

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request,'blog/login.html',{"forms":fm})
    else:
        return HttpResponseRedirect('/dashboard/')

# add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PostForm(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data['title']
                desc = fm.cleaned_data['desc']
                pst = blogPost(title=title,desc=desc)
                pst.save()
                fm=PostForm()
        else:
            fm = PostForm()
        return render(request,'blog/addpost.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/login/')


# Update POST
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = blogPost.objects.get(pk=id)
            fm = PostForm(request.POST,instance=pi)
            if fm.is_valid():
               fm.save()
        else:
            pi = blogPost.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/login/')


# Update POST
def delete_post(request,id):
    if request.user.is_authenticated:
        pi = blogPost.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
      


