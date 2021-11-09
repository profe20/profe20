from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin
from django.http import Http404, HttpResponse

from django.views.generic import  ListView ,DetailView
from contact.models import  Info

from .models import cairo
from.forms import cairoBookForm
##books
# Create your views here.


class cairoList(ListView):
    model=cairo




#filer


class cairoDetail(FormMixin,DetailView):
     model=cairo
     form_class =cairoBookForm
    ##books

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = cairo.objects.filter(category=self.get_object().category)[:2]
        # ^^^ bad duplication.
        return context

     def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
         try:
           myform = form.save(commit=False)
           myform.cairo=self.get_object()
           myform.user = request.user
           myform.save()
          except Article.DoesNotExist:
           raise Http404()

           return redirect('/')
