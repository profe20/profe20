from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.models import User


# Create your views here.
from django import forms
from .models import Post
from .forms  import PostForm
from django.conf.urls import url
from django.core.paginator import Paginator
from property.models import property ,place

def index(request):
 
    places=place.objects.all() 
   

    return render(request ,  'index.html',{
       'places' :places
        
    })


def ho_search(request):
    pass

def all_posts(request):
    all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'all_posts' :page_obj }

    return render(request ,  'all_posts.html',context)



def post(request,  id):
    #post= Post.objects.get(id=id)
    post = get_object_or_404( Post , id=id)

    context = {
         'post' : post ,
    }
    return render(request , 'datail.html',context)


def create_post(request):
    if request.method== 'POST':

        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
           new_form = form.save(commit=False)
           new_form.user = request.user
           new_form.save()
           return redirect('/')


    else:
         form = PostForm()

    context = {
        'form' : form ,
         }
    return render(request,'create.html',context)

def edit_post(request,  id):
    post = get_object_or_404( Post ,  id=id)
    if request.method== 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')


    else:
         form = PostForm(instance=post)

    context = {
        'form' : form ,
  }
    return render(request,'edit.html',context)
