from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('<int:id>/', views.food_detail, name='detail'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
]
