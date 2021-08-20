from django.shortcuts import render, get_list_or_404
from django.utils.translation import activate
from .models import Category, Comments, Post, Tag
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

def blogs(request):
    all = Post.objects.all().filter(status='publish')

    blog_page = Paginator(all, 1) # Show 1 contacts per page.
    page_number = request.GET.get('page')
    blog_list = blog_page.get_page(page_number)

    context = {
        'blog_list': blog_list,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    #detail = get_list_or_404(Post,slug=slug)
    detail = Post.objects.get(slug=slug)
    tags = Tag.objects.all().filter(blogs=detail)
    categorys = Category.objects.all().filter(blog=detail)
    recents = Post.objects.all().order_by('-pub_time')[:4]
    comm = Comments.objects.all().filter(comments=detail, active=True)

    posts_tags_ids = detail.tags.values_list('id', flat=True)
    post_similar = Post.objects.filter(tags__in=posts_tags_ids, status='publish').exclude(id=detail.id)
    post_similar = post_similar.annotate(same_tags=Count('tags')).order_by('-same_tags',)

    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.comments = detail
            new_comment.save()

        else:
            form = CommentForm()

    context = {
        'blog': detail,
        'tags': tags,
        'categorys': categorys,
        'recents': recents,
        'comments': comm,
        'form': form,
        'similar': post_similar,
    }
    return render(request, 'blog/blog_details.html', context)


def blog_tag(request, tag):
    all = Post.objects.filter(tags__slug=tag)
    context = {
        'blog_list' : all,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_category(request, category):
    all = Post.objects.filter(category__slug=category)
    context = {
        'blog_list' : all,
    }
    return render(request, 'blog/blog_list.html', context)


def search(request):
    if request.method == 'GET':
        res = request.GET.get('search')
    search_list = Post.objects.filter(title__icontains=res)

    blog_page = Paginator(search_list, 1)
    page_number = request.GET.get('page')
    blog_list = blog_page.get_page(page_number)

    content = {
        'blog_list': blog_list,
    }
    return render(request, 'blog/blog_list.html', content)




    




    