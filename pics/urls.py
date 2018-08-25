from django.urls import path
from . import views
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Post
from products import views as p_views

app_name = 'pics'

urlpatterns = [
    #/home/
    path('', views.index, name = 'index'),

    #/detail
    path('detail/<slug:slug>/', DetailView.as_view(
        model=Post, template_name='pics/detail.html')),

    #/archive/
    path('archive/', ListView.as_view(queryset = Post.objects.all().order_by('-pub_date'), 
    template_name = 'pics/archive.html')),

    #/about/
    path('about/', views.about, name ='about'),

    #/store/
    path('store/', p_views.product_list, name ='store'),
]