from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from .forms import CommentForm


from django.views.generic import  ListView ,DetailView

# Create your views here.
from django import forms
from .models import Post
from .forms  import PostForm
from django.conf.urls import url
from django.core.paginator import Paginator
from property.models import property ,place
from aswan .models import aswan
from luxortour .models import luxortour
from cairotour  .models import cairotour
from  nilecruise  .models import  nilecruise
from  contact  .models import  Info
from  packages  .models import  packages
from django.http import HttpResponse
from .models import slideImages
from .models import Comment
from .forms import CommentForm

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)



def index(request):


    Propertyrft = Post.objects.all()
    Propertyryt = luxortour.objects.all()[:3]
    aswanss = aswan.objects.all()[:3]
    cairoo = cairotour.objects.all()[:4]
    packagess = packages.objects.all()[:3]
    Infoo = Info.objects.all()[:1]
    Nilecruisee = nilecruise.objects.all()[:3]
    Infoo = Info.objects.all()
    Propertyrytt = property.objects.all()[:3]


    comments = Comment.objects.filter(active=True)[:2]

    slideImagess = slideImages.objects.all()[:1]

    if request.method== 'POST':

         comment_form = CommentForm(request.POST , request.FILES)
         if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.user = request.user
            comment_form.save()
            return redirect('/')


    else:
          comment_form = CommentForm()



    return render(request ,  'index.html',{

       'Propertyrft' : Propertyrft,
       'Propertyryt' : Propertyryt,
       'aswanss' : aswanss,
       'cairoo' : cairoo,
       'Nilecruisee' : Nilecruisee,
       'packagess' : packagess,
       'Infoo' : Infoo,
      'slideImagess' : slideImagess,
      'comments' : comments,
     'comment_form': comment_form,
      'Propertyrytt': Propertyrytt
    })



def baset(request):
    all_posts = Post.objects.filter(active=True)
    Infooo = Info.objects.all()


    return render(request ,  'baset.html',{

       'Infooo' : Infooo,

    })


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

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, Comment, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
