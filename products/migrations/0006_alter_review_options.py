# Generated by Django 3.2.20 on 2023-08-10 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-is_featured',)},
        ),
    ]