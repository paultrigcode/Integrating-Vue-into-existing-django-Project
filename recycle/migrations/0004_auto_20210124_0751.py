# Generated by Django 3.1.5 on 2021-01-24 07:51

from django.db import migrations, models
import recycle.models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0003_auto_20210124_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recycler',
            name='customer_number',
            field=models.CharField(default=recycle.models.increment_invoice_number, max_length=1000000000),
        ),
    ]
