# Generated by Django 3.0.8 on 2020-09-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0029_auto_20200908_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_one',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_three',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_two',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='approval',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='citizenship',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]
