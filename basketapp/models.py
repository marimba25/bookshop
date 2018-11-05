from django.db import models
from django.conf import settings
from mainapp.models import Book


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return str(self.product)

    def get_product_cost(self):
        return self.product.price * self.quantity

    product_cost = property(get_product_cost)

    def get_total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        totalquantity = sum(list(map(lambda x: x.quantity, items)))
        return totalquantity

    total_quantity = property(get_total_quantity)

    def get_total_cost(self):
        items = Basket.objects.filter(user=self.user)
        totalcost = sum(list(map(lambda x: x.product_cost, items)))
        return totalcost

    total_cost = property(get_total_cost)

    @staticmethod
    def get_items(user):
        return user.basket_set.all()

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()
