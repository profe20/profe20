from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin

from django.views.generic import  ListView ,DetailView
from contact.models import  Info
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .models import packages,Comment
from.forms import packagesBookBookForm,CommentForm
##books
from .forms import CommentForm
# Create your views here.


class packagesList(ListView):
    model=packages




#filer


class packagesDetail(FormMixin,DetailView):
     model=packages
     form_class =packagesBookBookForm
    ##books

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = packages.objects.filter(category=self.get_object().category)[:2]
        # ^^^ bad duplication.
        return context
     @method_decorator(login_required(login_url='/accounts/login/'))
     def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
           myform = form.save(commit=False)
           myform.packages=self.get_object()
           myform.user = request.user
           myform.save()
           return redirect('/')



        def post(self, request, *args, **kwargs):
           form = self.get_form()

           if form.is_valid():
              myform = form.save(commit=False)
              myform.packages=self.get_object()
              myform.user = request.user
              myform.save()
              return redirect('/')
