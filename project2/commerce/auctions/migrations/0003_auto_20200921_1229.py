# Generated by Django 3.0.3 on 2020-09-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_comments_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fa', 'Fashion'), ('To', 'Toys'), ('El', 'Electronics'), ('Ho', 'Home'), ('Cl', 'clothes'), ('Ot', 'Other')], default=('Ot', 'Other'), max_length=64, verbose_name='Category '),
        ),
        migrations.AlterField(
            model_name='listing',
            name='currentprice',
            field=models.IntegerField(verbose_name='Price '),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(verbose_name='Description '),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(upload_to='biduploads/%Y/%m/%d/', verbose_name='Picture of item '),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Item '),
        ),
    ]
