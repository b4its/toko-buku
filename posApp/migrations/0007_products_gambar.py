# Generated by Django 3.2.12 on 2022-07-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0006_delete_buku'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='gambar',
            field=models.FileField(blank=True, null=True, upload_to='produk'),
        ),
    ]
