# Generated by Django 4.0.4 on 2022-05-25 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_order_delivery_method_remove_order_manager_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'ordering': ['auto_increment_id']},
        ),
    ]