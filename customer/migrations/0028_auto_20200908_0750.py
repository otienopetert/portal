# Generated by Django 3.0.8 on 2020-09-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0027_auto_20200907_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_one',
            field=models.ImageField(blank=True, default='layout_set_logo.png', editable=False, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_three',
            field=models.ImageField(blank=True, default='layout_set_logo.png', editable=False, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='another_two',
            field=models.ImageField(blank=True, default='layout_set_logo.png', editable=False, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='approval',
            field=models.ImageField(blank=True, default='layout_set_logo.png', editable=False, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='citizenship',
            field=models.ImageField(blank=True, default='layout_set_logo.png', editable=False, null=True, upload_to=''),
        ),
    ]
