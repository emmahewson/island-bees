# Generated by Django 3.2.20 on 2023-09-19 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_discontinued'),
        ('checkout', '0006_auto_20230919_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lineitems', to='products.product'),
        ),
    ]
