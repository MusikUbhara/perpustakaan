# Generated by Django 4.1.11 on 2023-09-11 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='sampul_buku',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='buku',
            name='thumbnail_sampul',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
