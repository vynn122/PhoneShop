# Generated by Django 5.1.5 on 2025-02-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0005_rename_customer_cart_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='discountPercentange',
            field=models.IntegerField(blank=True, choices=[(0, '0%'), (5, '5%'), (10, '10%'), (15, '15%'), (20, '20%'), (25, '25%'), (50, '50%'), (75, '75%'), (100, '100%')], null=True),
        ),
    ]
