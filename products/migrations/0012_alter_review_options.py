# Generated by Django 3.2.20 on 2023-08-10 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_review_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-is_featured', 'created_on')},
        ),
    ]
