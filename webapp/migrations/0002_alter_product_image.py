# Generated by Django 3.2 on 2021-05-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='user_pics', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]
