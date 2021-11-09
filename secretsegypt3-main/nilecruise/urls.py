from django.conf.urls import url
from . import views
from django.urls import include, path

from.views import  nilecruiseList,nilecruiseDetail

app_name = 'nilecruise'

urlpatterns  = [

    path('', nilecruiseList.as_view(),name='cnilecruise_list'),
    path( '<slug:slug>' ,nilecruiseDetail. as_view(),name='nilecruise_detail'),


]
