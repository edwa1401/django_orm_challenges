import json
from django.db import models
from django.utils.translation import gettext_lazy as _
from typing import Any

class Book(models.Model):
    title = models.CharField(max_length=256)
    author_full_name = models.CharField(max_length=256)
    isbn = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Laptop(models.Model):

    class Brand(models.TextChoices):
        LENOVO = 'LENOVO'
        HONOR = 'HONOR'
        APPlE = 'APPLE'
    
    brand_name = models.CharField(
        choices = Brand.choices,
        max_length=100
    )
    year_of_issue = models.SmallIntegerField(
        help_text='year_of issue'
    )
    ram_volume = models.PositiveSmallIntegerField(
        help_text='ram volume in GB'
    )
    hdd_capacity = models.DecimalField(
        decimal_places=3,
        max_digits=10,
        help_text='hdd capacity in GB'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    stock_count = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self) -> str:
        return f'{self.brand_name}, {self.stock_count}'

    def to_json(self) -> dict[str, Any]:
        return {
                'brand_name': self.brand_name,
                'year_of_issue': self.year_of_issue,
                'ram_volume': self.ram_volume,
                'hdd_capacity': float(self.hdd_capacity),
                'price': float(self.price),
                'stock_count': self.stock_count,
                'created_at': str(self.created_at),
        }


class Post(models.Model):
    class Meta:
        get_latest_by = 'published_at',
        ordering = ['-published_at']

    class Status(models.TextChoices):
        PUBLISHED = 'PUBLISHED'
        NOT_PUBLISHED = 'NOT_PUBLISHED'
        BANNED = 'BANNED'

    class Category(models.TextChoices):
        CULTURE = 'CL', _('Culture')
        SPORT = 'SP', _('Sport')
        POLITIC = 'PL', _('Politic')
        __empty__ = ('(Unknown)')
    
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    status = models.CharField(
        choices=Status.choices,
        default=Status.NOT_PUBLISHED,
        max_length=100
        )
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    category = models.CharField(choices=Category.choices, max_length=100, )

    def __str__(self) -> str():
        return f'{self.title}, published at {self.published_at}'

    def to_json(self) -> dict[str, Any]:
        return {
                'title': self.title,
                'text': self.text,
                'author': self.author,
                'status': self.status,
                'created_at': str(self.created_at),
                'published_at': str(self.published_at),
                'category': self.category,
            }
    
        