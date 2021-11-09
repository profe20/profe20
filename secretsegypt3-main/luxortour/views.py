from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


from django.views.generic import  ListView ,DetailView

from .models import luxortour
from.forms import luxortourBookForm
# Create your views here.


class luxortourList(ListView):
    model=luxortour
    ##filer


class luxortouryDetail(FormMixin,DetailView):
     model=luxortour
     form_class =luxortourBookForm
    ##books

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = luxortour.objects.filter(category=self.get_object().category)[:2]
        # ^^^ bad duplication.
        return context
     @method_decorator(login_required(login_url='/accounts/login/'))
     def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
           myform = form.save(commit=False)
           myform.luxortour=self.get_object()
           myform.user = request.user
           myform.save()
           return redirect('/')
