from django.conf.urls import url
from . import views
from django.urls import include, path

from.views import  PropertyList,propertyDetail

app_name = 'property'

urlpatterns  = [
    
    url( '' , PropertyList, as_view()),
    #url( '' , propertyDetail, as_view()),

   


]
