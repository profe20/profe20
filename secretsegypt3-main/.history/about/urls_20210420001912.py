from django.conf.urls import url
from . import views
from django.urls import include, path

from.views import  aboutList

app_name = 'about'

urlpatterns  = [
     
    path('', aboutList.as_view(),name='aboutList'),
   
]