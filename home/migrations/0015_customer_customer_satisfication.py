# Generated by Django 3.0.1 on 2019-12-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_satisfication',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
