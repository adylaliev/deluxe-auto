from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from products.models import Product

User = get_user_model()


class RatingStar(models.Model):
    value = models.SmallIntegerField('value', default=0)

    def str(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Rating Star'
        verbose_name_plural = 'Rating Stars'
        ordering = ['-value']


class Rating(models.Model):
    ads = models.ForeignKey(Product, on_delete=models.CASCADE,
                            related_name='rating')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='rating')
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE,
                             related_name='rating')

    def str(self):
        return f'{self.star} - {self.ads}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Likes(models.Model):
    liked = models.ForeignKey(Product, on_delete=models.CASCADE,
                                  related_name='ads_likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_likes')