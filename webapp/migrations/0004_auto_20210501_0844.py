# Generated by Django 3.2 on 2021-05-01 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзывы', 'verbose_name_plural': 'Отзыв'},
        ),
        migrations.AlterModelTable(
            name='review',
            table='Reviews',
        ),
    ]
