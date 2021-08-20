from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<slug:slug>', views.blog_detail, name='detail'),
    path('tag/<slug:tag>', views.blog_tag, name='tag'),
    path('category/<slug:category>', views.blog_category, name='category'),
    path('search/', views.search, name='search'),
]
