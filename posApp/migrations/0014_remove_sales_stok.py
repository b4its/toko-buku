# Generated by Django 3.2.14 on 2022-07-31 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0013_auto_20220731_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='stok',
        ),
    ]
