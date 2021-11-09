from django.conf.urls import url
from . import views
from django.urls import include, path

from.views import  PropertyList,propertyDetail

app_name = 'property'

urlpatterns  = [
     
    path('', PropertyList.as_view(),name='property_list'),
    path( '<slug:slug>' ,propertyDetail. as_view(),name='property_detail'),
   
]
