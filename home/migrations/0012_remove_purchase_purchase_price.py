# Generated by Django 3.0.1 on 2019-12-21 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_price',
        ),
    ]
