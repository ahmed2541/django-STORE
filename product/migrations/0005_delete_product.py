# Generated by Django 4.1.2 on 2022-10-14 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_orderitem_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
