# Generated by Django 3.0.1 on 2019-12-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191229_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_rfm',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_value',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=40),
        ),
    ]
