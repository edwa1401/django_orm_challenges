"""
В этом задании вам предстоит работать с моделью ноутбука. У него есть бренд (один из нескольких вариантов),
год выпуска, количество оперативной памяти, объём жесткого диска, цена, количество этих ноутбуков на складе
и дата добавления.

Ваша задача:
- создать соответствующую модель (в models.py)
- создать и применить миграцию по созданию модели (миграцию нужно добавить в пул-реквест)
- заполнить вашу локальную базу несколькими ноутбуками для облегчения тестирования
  (я бы советовал использовать для этого shell)
- реализовать у модели метод to_json, который будет преобразовывать объект книги в json-сериализуемый словарь
- по очереди реализовать каждую из вьюх в этом файле, проверяя правильность их работу в браузере
"""
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from challenges.models import Laptop
import decimal


def laptop_details_view(request: HttpRequest, laptop_id: int) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть json-описание ноутбука по его id.
    Если такого id нет, вернуть 404.
    """

    laptop = get_object_or_404(Laptop, id=laptop_id)
    return JsonResponse(laptop.to_json(), safe=False)


def laptop_in_stock_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть json-описание всех ноутбуков, которых на складе больше нуля.
    Отсортируйте ноутбуки по дате добавления, сначала самый новый.
    """
    newest_laptops = Laptop.objects.filter(stock_count__gt=0).order_by('-created_at')
    serialised_laptops = [laptop.to_json() for laptop in newest_laptops]
    return JsonResponse(serialised_laptops, safe=False)


def laptop_filter_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть список ноутбуков с указанным брендом и указанной минимальной ценой.
    Бренд и цену возьмите из get-параметров с названиями brand и min_price.
    Если бренд не входит в список доступных у вас на сайте или если цена отрицательная, верните 403.
    Отсортируйте ноутбуки по цене, сначала самый дешевый.
    """
    brand = request.GET.get('brand_name')
    min_price = decimal.Decimal(request.GET.get('min_price'))
    targeted_laptops = Laptop.objects.filter(
        brand_name=brand,
        price__gte=min_price
        ).order_by('price')
    if not targeted_laptops or min_price < 0:
        return HttpResponseForbidden('No such brand or price is negative')
    
    serialised_laptops = [laptop.to_json() for laptop in targeted_laptops]
    return JsonResponse(serialised_laptops, safe=False)
    


def last_laptop_details_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть json-описание последнего созданного ноутбука.
    Если ноутбуков нет вообще, вернуть 404.
    """
    last_laptop = Laptop.objects.order_by('created_at').last()
    if not last_laptop:
        return HttpResponseNotFound('no notebooks')
    return JsonResponse(last_laptop.to_json(), safe=False)
