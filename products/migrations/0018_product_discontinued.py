# Generated by Django 3.2.20 on 2023-09-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discontinued',
            field=models.BooleanField(default=False),
        ),
    ]
