# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404
from .models import Post, Category, Location

# Главная страница
def index(request):
    # Получаем только опубликованные записи, которые не позже текущего времени, и у которых категория опубликована
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]  # Ограничиваем 5 последними записями

    return render(request, 'blog/index.html', {'post_list': posts})

# Детали поста
def post_detail(request, id):
    # Получаем публикацию по id
    post = get_object_or_404(Post, id=id)

    # Проверяем, опубликована ли публикация
    if not post.is_published:
        raise Http404("Публикация не опубликована")

    # Проверяем, что дата публикации не позже текущего времени
    if post.pub_date > timezone.now():
        raise Http404("Публикация еще не доступна")

    # Проверяем, что категория публикации опубликована
    if not post.category.is_published:
        raise Http404("Категория публикации не опубликована")

    return render(request, 'blog/detail.html', {'post': post})

# Посты по категории
def category_posts(request, category_slug):
    # Получаем категорию по slug
    category = get_object_or_404(Category, slug=category_slug)

    # Проверяем, опубликована ли категория
    if not category.is_published:
        raise Http404("Категория не опубликована")

    # Фильтруем публикации по выбранной категории
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    return render(request, 'blog/category.html', {'category': category, 'post_list': posts})