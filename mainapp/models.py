from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255,
                             default='Книга',
                             verbose_name='Наименование произведения')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Стоимость товара', null=True)
    counts_of_sheets = models.PositiveIntegerField(verbose_name='Количество страниц')
    photo = models.ImageField(upload_to='bookshop/media',
                              null=True,
                              blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255, default='Автор', verbose_name='Имя автора')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна автора')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, default='Страна автора', verbose_name='Страна автора')

    def __str__(self):
        return self.name