# Generated by Django 5.0.6 on 2024-05-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='order_date',
            field=models.DateField(),
        ),
    ]
