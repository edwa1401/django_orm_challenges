"""
В этом задании вам предстоит работать с моделью поста в блоге. У него есть название, текст, имя автора, статус
(опубликован/не опубликован/забанен), дата создания, дата публикации, категория (одна из нескольких вариантов).

Ваша задача:
- создать соответствующую модель (в models.py)
- создать и применить миграцию по созданию модели (миграцию нужно добавить в пул-реквест)
- заполнить вашу локальную базу несколькими ноутбуками для облегчения тестирования
- реализовать у модели метод to_json, который будет преобразовывать объект книги в json-сериализуемый словарь
- по очереди реализовать каждую из вьюх в этом файле, проверяя правильность их работу в браузере
"""
from django.http import HttpRequest, HttpResponse, JsonResponse
from challenges.models import Post
import datetime
from typing import Any
from django.db.models import Q

def posts_to_json(posts: Post) -> list[dict[str, Any]]:
    return [post.to_json() for post in posts]

def last_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть 3 последних опубликованных поста.    
    """
    last_posts = Post.objects.filter(status='PUBLISHED')[:3]
    serialized_posts = posts_to_json(last_posts)
    return JsonResponse(serialized_posts, safe=False, json_dumps_params={'ensure_ascii': False},) 


def posts_search_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты, которые подходят под поисковый запрос.
    Сам запрос возьмите из get-параметра query.
    Подходящесть поста можете определять по вхождению запроса в название или текст поста, например.
    """
    search_word = request.GET.get('search_text')
    searched_posts = Post.objects.filter(
        Q(title__icontains=search_word)|
        Q(text__icontains=search_word)
        )

    serialized_posts = posts_to_json(searched_posts)
    return JsonResponse(serialized_posts, safe=False, json_dumps_params={'ensure_ascii': False},)
       
def untagged_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты без категории, отсортируйте их по автору и дате создания.
    """
    posts_without_category = Post.objects.filter(category='').order_by('author', 'created_at')
    serialized_posts = posts_to_json(posts_without_category)
    return JsonResponse(serialized_posts, safe=False, json_dumps_params={'ensure_ascii': False},)


def categories_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты все посты, категория которых принадлежит одной из указанных.
    Возьмите get-параметр categories, в нём разделённый запятой список выбранных категорий.
    """
    categories = request.GET.get('categories').split(", ")

    posts_within_categories = Post.objects.filter(category__in = categories)
    serialized_posts = posts_to_json(posts_within_categories)
    return JsonResponse(serialized_posts, safe=False, json_dumps_params={'ensure_ascii': False},)


def last_days_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть посты, опубликованные за последние last_days дней.
    Значение last_days возьмите из соответствующего get-параметра.
    """
    last_day = float(request.GET.get('last_days'))
    first_day = datetime.datetime.now() - datetime.timedelta(days=last_day)
    last_day_posts = Post.objects.filter(published_at__gte=first_day)
    serialized_posts = posts_to_json(last_day_posts)
    return JsonResponse(serialized_posts, safe=False, json_dumps_params={'ensure_ascii': False},)
