from django.conf.urls import url
from . import views
from django.urls import include, path

from.views import packagesList,packagesDetail

app_name = 'packages'

urlpatterns  = [

    path('', packagesList.as_view(),name='packages_list'),
    path( '<slug:slug>' ,packagesDetail. as_view(),name='packages_detail'),


]
