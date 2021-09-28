from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    name = models.CharField('Заголовок', max_length=255, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='', blank=True)
    text = models.TextField('Описание')
    price = models.DecimalField(max_digits=100, decimal_places=0)
    status = models.CharField('Статусы', max_length=10)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='prod', verbose_name='Автор')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    update_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

        def __str__(self):
            return self.name


class Basket(models.Model):
    value = models.SmallIntegerField('value', default=0)

    def str(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['-value']


class Purchases(models.Model):
    ads = models.ForeignKey(Product, on_delete=models.CASCADE,
                            related_name='rating')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='rating')
    star = models.ForeignKey(Basket, on_delete=models.CASCADE,
                             related_name='rating')

    def str(self):
        return f'{self.star} - {self.ads}'

    class Meta:
        verbose_name = 'покупка'
        verbose_name_plural = 'покупки'