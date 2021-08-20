from django.contrib import admin
from . models import Food

# Register your models here.

@admin.register(Food)
class AdminFood(admin.ModelAdmin):
    list_display = ('name', 'rate', 'price')
    list_filter = ('price', 'rate', 'status')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

