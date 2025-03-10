# Generated by Django 5.1.5 on 2025-02-09 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0010_alter_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ShopApp.customer')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopApp.phone')),
            ],
        ),
    ]
