# Generated by Django 5.0.6 on 2024-07-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_dessert_delete_menu_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sea_Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена блюда')),
                ('image', models.ImageField(upload_to='menu_images/', verbose_name='Фото блюда')),
                ('category', models.CharField(max_length=50, verbose_name='Категория блюда')),
            ],
            options={
                'verbose_name_plural': 'Морепродукты',
            },
        ),
    ]