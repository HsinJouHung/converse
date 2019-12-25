# Generated by Django 3.0.1 on 2019-12-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191221_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_tel', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=20)),
                ('customer_age', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=10)),
                ('num_familymembers', models.CharField(max_length=10)),
                ('register_date', models.CharField(max_length=10)),
                ('monthly_income', models.CharField(max_length=20)),
            ],
        ),
    ]
