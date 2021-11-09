from django.conf.urls import url
from . import views
from django.urls import include, path
from django.contrib.auth.decorators import login_required

from.views import  cairotourList,cairotourDetail,cairotourBookForm

app_name = 'cairotour'

urlpatterns  = [

    path('', cairotourList.as_view(),name='cairotour_list'),
    path( '<slug:slug>' ,cairotourDetail. as_view(),name='cairotour_detail'),
    path('createe',views.cairotourBookForm, name='cairotourBookForm'),



]
