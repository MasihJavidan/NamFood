from django.contrib import admin
from .models import Category, Comments, Post, Tag

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_time',)
    list_filter = ('pub_time',)
    search_fields = ('title', 'author', 'description')


@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    list_display = ('name', 'email', 'comments','active')
    list_filter = ('active', 'pub_time', 'edit')
    search_fields = ('name', 'email', 'comments', 'content')


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
