# Generated by Django 3.2.7 on 2021-09-24 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('text', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=10, max_digits=100)),
                ('status', models.CharField(choices=[('open', 'Открытое'), ('closed', 'Закрытое'), ('draft', 'Черновик')], max_length=10, verbose_name='Статусы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата объявления')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
    ]