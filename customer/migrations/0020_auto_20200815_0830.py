# Generated by Django 3.0.8 on 2020-08-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0019_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businesscategory', models.CharField(choices=[('Tanzanian', 'Tanzanian'), ('Foreigner', 'Foreigner')], max_length=200, null=True)),
                ('price', models.FloatField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='businesscategory',
            field=models.CharField(choices=[('Tanzanian', 'Tanzanian'), ('Foreigner', 'Foreigner')], max_length=200, null=True),
        ),
    ]
