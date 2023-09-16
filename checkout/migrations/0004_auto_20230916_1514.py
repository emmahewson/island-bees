# Generated by Django 3.2.20 on 2023-09-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(default='Isle of Anglesey', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default='AA11 2BB', max_length=20),
            preserve_default=False,
        ),
    ]
