# Generated by Django 3.0.8 on 2020-07-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
