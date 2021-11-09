from django.conf.urls import url
from . import views
from django.urls import include, path

from.views import  luxortourList,luxortouryDetail

app_name = 'luxortour'

urlpatterns  = [

    path('', luxortourList.as_view(),name='luxortour_list'),
    path( '<slug:slug>' ,luxortouryDetail. as_view(),name='luxortour_detail'),

]
