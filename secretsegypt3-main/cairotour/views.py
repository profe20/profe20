from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.views.generic import  ListView ,DetailView
from django.urls import reverse_lazy

from .models import cairotour
from.forms import cairotourBookForm
# Create your views here.


class cairotourList(ListView):
    model=cairotour
    ##filer


class cairotourDetail(FormMixin,DetailView):
     model=cairotour
     form_class =cairotourBookForm

    ##books

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = cairotour.objects.filter(category=self.get_object().category)[:2]
        # ^^^ bad duplication.
        return context


     @method_decorator(login_required(login_url='/accounts/login/'))
     def post(self, request, *args, **kwargs):

         form = self.get_form()

         if form.is_valid():

           myform = form.save(commit=False)
           myform.cairotour=self.get_object()
           myform.user = request.user
           myform.save()
           return redirect('/')
