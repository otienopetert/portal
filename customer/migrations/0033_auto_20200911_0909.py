# Generated by Django 3.0.8 on 2020-09-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0032_auto_20200911_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_one',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_two',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='approval',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='citizenship',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
