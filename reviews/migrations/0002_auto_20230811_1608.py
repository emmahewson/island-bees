# Generated by Django 3.2.20 on 2023-08-11 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-rating', 'created_on')},
        ),
        migrations.RemoveField(
            model_name='review',
            name='is_featured',
        ),
    ]
