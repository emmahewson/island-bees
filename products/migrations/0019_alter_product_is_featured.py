# Generated by Django 3.2.20 on 2023-09-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_discontinued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]