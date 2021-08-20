from django.shortcuts import render, get_list_or_404
from .models import Food
from django.views.generic import TemplateView


# Create your views here.

def food_list(requests):
    food_list = Food.objects.all()
    context = {
        'foods' : food_list
    }
    return render(requests, 'food/list.html', context)



def food_detail(requests, id):
    food_detail = Food.objects.get(id = id)
    context = {
        'food' : food_detail
    }
    return render(requests, 'food/detail.html', context)


def about(request):
    food_list = Food.objects.all
    context = {
        'foods' : food_list
    }
    return render(request, 'food/about.html', context)

def gallery(request):
    food_list = Food.objects.all()
    context = {
        'foods' : food_list
    }
    return render(request, 'food/gallery.html', context)



