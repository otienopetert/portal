# Generated by Django 3.0.8 on 2020-08-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantdetails',
            name='addressinfo',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicantdetails',
            name='nationality',
            field=models.CharField(choices=[('Tanzanian', 'Tanzanian'), ('Foreigner', 'Foreigner')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]