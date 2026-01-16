from django.shortcuts import render , redirect
from blogs.models import Category , Blog
from assignment.models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
def home(request):
    featured_post=Blog.objects.filter(is_featured=True , status='Published')
    posts=Blog.objects.filter(is_featured=False , status='Published')
    # categories=Category.objects.all().order_by('updated_at')
    try:
        
        about_us=AboutUs.objects.get()
    except:
        about_us=None     
    # try:
    #     follow_us=FollowUs.objects.get()
    # except:
    #     follow_us=None
    context={
        
        'featured_post':featured_post,
        'posts':posts, 
        'about_us' : about_us,
        # 'follow_us' : follow_us
    }
    return render(request , 'home.html' , context)


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=RegistrationForm()
    context={
        'form': form
    }
    return render(request , 'register.html' , context)

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request , user)
                return redirect('dashboard') 
    else:       
        form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request , 'login_view.html' , context)

def logout_view(request):
    logout(request)
    return redirect('home')