# Generated by Django 3.0.8 on 2020-09-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0036_uploaddocuments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddocuments',
            name='pdf1',
            field=models.FileField(upload_to=''),
        ),
    ]