from django.shortcuts import render , redirect
from blogs.models import Category , Blog
from django.contrib.auth.decorators import login_required
from .forms import *
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login_view')
def dashboard(request):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blogs_count
    }
    return render(request , 'dashboard/dashboard.html' , context)
 
def categories(request):
     return render(request , 'dashboard/categories.html')

def add_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:    
        form=CategoryForm()
    context={
        'form':form
    }
    return render(request , 'dashboard/add_category.html' , context) 


def edit_category(request , category_id):
    category=Category.objects.get(id=category_id)
    if request.method=="POST": 
        form=CategoryForm(request.POST , instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form=CategoryForm(instance=category)
        context={
            'form':form
        }
        return render(request , 'dashboard/edit_category.html' , context)
    
def delete_category(request , category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories')


def blogs(request):
    return render(request , 'dashboard/blogs.html')


def add_blogs(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()  # unique slug will be created automatically
            return redirect('blogs')

    else:
        form = BlogForm()

    return render(request, 'dashboard/add_blogs.html', {'form': form})



def edit_blog(request, blog_id ):
    blog=Blog.objects.get(id=blog_id)
    # form=BlogForm(request.POST, request.FILES , instance=blog_id)
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES , instance=blog)
        if form.is_valid():
            blog=form.save()
            title=form.cleaned_data['title']
            blog.slug=slugify(title) + '-'+str(blog.id)
            blog.save()
            return redirect('blogs')
    else:
        form=BlogForm(instance=blog)
    context={
        'form':form,
        'blog':blog
 
    }
    return render(request , 'dashboard/edit_blog.html', context)


def delete_blog(request , blog_id):
    blog=Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('blogs')


def users(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request , 'dashboard/users.html' , context)



def add_users(request):
    if request.method=='POST':
        form=AdduserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:    
        form= AdduserForm()
    context={
        'form':form
    }
    return render(request , 'dashboard/add_users.html' , context )



def edit_users(request , user_id):
    user=User.objects.get(id=user_id)
    if request.method=="POST":
        form=EditUserForm(request.POST , instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")
        
    else:
        form=EditUserForm(instance=user)
    context={
        'form':form
    }
    return render(request , 'dashboard/edit_users.html' , context)


def delete_users(request , user_id):
    user=User.objects.get(id=user_id)
    user.delete()
    return redirect('users')
