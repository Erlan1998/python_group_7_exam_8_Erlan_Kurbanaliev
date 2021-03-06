from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
category_choices = [('other', 'Разное'), ('sports', 'Спортивне'),  ('Classic', 'Классические'), ('For home', 'Для дома'), ('for study', 'Для учебы')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=category_choices)
    description = models.TextField(max_length=2000, null=False, blank=True)
    image = models.ImageField(null=False, blank=True, upload_to='user_pics', verbose_name='Картинка')

    class Meta:
        db_table = 'Products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.id}. {self.name}'


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='Reviews', on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    product = models.ForeignKey('webapp.Product', related_name='Reviews', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    moderated = models.BooleanField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Reviews'
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'

    def __str__(self):
        return f'{self.id}. {self.user}'