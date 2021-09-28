# Generated by Django 3.2.7 on 2021-09-28 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='value')),
            ],
            options={
                'verbose_name': 'Rating Star',
                'verbose_name_plural': 'Rating Stars',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='products.product')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL)),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='orders.ratingstar')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_likes', to=settings.AUTH_USER_MODEL)),
                ('liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads_likes', to='products.product')),
            ],
        ),
    ]