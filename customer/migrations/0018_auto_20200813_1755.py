# Generated by Django 3.0.8 on 2020-08-14 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20200811_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='amount',
            field=models.FloatField(max_length=200, null=True),
        ),
    ]
