# Generated by Django 3.0.8 on 2020-07-31 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20200731_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
