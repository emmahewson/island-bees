# Generated by Django 3.2.20 on 2023-08-10 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-is_featured', '-rating')},
        ),
    ]