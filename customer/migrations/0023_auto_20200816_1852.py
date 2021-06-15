# Generated by Django 3.0.8 on 2020-08-17 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='logo',
            field=models.ImageField(blank=True, default='layout_set_logo.png', editable=False, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='uploaddocuments',
            name='another_one',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='uploaddocuments',
            name='another_three',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='uploaddocuments',
            name='another_two',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='uploaddocuments',
            name='approval',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='uploaddocuments',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Customer'),
        ),
        migrations.AlterField(
            model_name='uploaddocuments',
            name='citizenship',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
