from django.conf.urls import url
from . import views  
from.views import  PropertyList,propertyDetail

app_name = 'Post'


urlpatterns  = [
    url( r'^$' , views.index , name='index'),
    url('all_posts' , views.all_posts , name='all_posts'),
    url(r'^(?P<id>\d+)$', views.post , name='post'),
    url('create',views.create_post, name='create_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post ,name='edit_post'),
    url('search' , home_search , name='home_search'),
    

]
