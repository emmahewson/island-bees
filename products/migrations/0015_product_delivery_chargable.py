# Generated by Django 3.2.20 on 2023-09-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery_chargable',
            field=models.BooleanField(default=True),
        ),
    ]
