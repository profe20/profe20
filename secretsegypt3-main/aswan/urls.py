from django.conf.urls import url
from . import views
from django.urls import include, path

from.views import  aswanList,aswanDetail,Info_List

app_name = 'aswan'

urlpatterns  = [

    path('', aswanList.as_view(),name='aswan_list'),
    path('Info_List' , views.Info_List , name='Info_List'),
    path( '<slug:slug>' ,aswanDetail. as_view(),name='aswan_detail'),


]
