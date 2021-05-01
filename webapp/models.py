from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
category_choices = [('other', 'Разное'), ('sports', 'Спортивне'),  ('Classic', 'Классические'), ('For home', 'Для дома'), ('for study', 'Для учебы')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=category_choices)
    description = models.TextField(max_length=2000, null=False, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    class Meta:
        db_table = 'Products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.id}. {self.name}'
