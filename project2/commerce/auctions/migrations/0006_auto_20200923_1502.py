# Generated by Django 3.0.3 on 2020-09-23 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200923_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='publishdate',
            field=models.DateField(auto_created=datetime.datetime(2020, 9, 23, 15, 2, 8, 833843), default=datetime.datetime(2020, 9, 23, 15, 2, 8, 833843)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Home', 'Home'), ('Clothes', 'Clothes'), ('Food', 'Food'), ('Shoes', 'Shoes'), ('Other', 'Other')], default=('Other', 'Other'), max_length=64, verbose_name='Category '),
        ),
    ]