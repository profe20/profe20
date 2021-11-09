from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import  ListView ,DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from  contact  .models import  Info

from .models import aswan
from.forms import aswanyBookForm
##books
# Create your views here.


class aswanList(ListView):
    model=aswan



def Info_List(request):
    Info_List = Info.objects.all()


    context = {'Info_List' :Info_List }

    return render(request ,  'Info_List.html',context)




class aswanDetail(FormMixin,DetailView):
     model=aswan
     form_class =aswanyBookForm
    ##books

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = aswan.objects.filter(category=self.get_object().category)[:2]
        # ^^^ bad duplication.
        return context
     @method_decorator(login_required(login_url='/accounts/login/'))
     def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
           myform = form.save(commit=False)
           myform.aswan=self.get_object()
           myform.user = request.user
           myform.save()
           return redirect('/')
