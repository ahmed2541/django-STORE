# Generated by Django 4.1 on 2022-10-14 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
    ]