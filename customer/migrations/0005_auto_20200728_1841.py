# Generated by Django 3.0.8 on 2020-07-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200728_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicantdetails',
            name='dob',
        ),
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
