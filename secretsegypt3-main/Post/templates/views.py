from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin

from django.views.generic import  ListView

from .models import about
from .models import gallery
# Create your views here.


class aboutList(ListView):
    model=about
    ##filer



def gallery_List(request):
    gallery_List = gallery.objects.all()

    page_number = request.GET.get('page')

    context = {'gallery_List' :gallery_List }

    return render(request ,  'gallery_List.html',context)
