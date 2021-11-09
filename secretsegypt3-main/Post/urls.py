from django.conf.urls import url
from . import views


app_name = 'Post'


urlpatterns  = [
    url( r'^$' , views.index , name='index'),
    url( 'baset' , views.baset , name='baset'),
    url('all_posts' , views.all_posts , name='all_posts'),
    url(r'^(?P<id>\d+)$', views.post , name='post'),
    url('create',views.create_post, name='create_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post ,name='edit_post'),
    url('<slug:slug>/', views.post_detail, name='post_detail')




]
