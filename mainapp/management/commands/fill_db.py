from django.core.management.base import BaseCommand
from mainapp.models import BookCategory, Book
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        BookCategory.objects.all().delete()
        for category in categories:
            new_category = BookCategory(**category)
            new_category.save()

        products = loadFromJSON('products')

        Book.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = BookCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            Book['category'] = _category
            new_product = Book(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
