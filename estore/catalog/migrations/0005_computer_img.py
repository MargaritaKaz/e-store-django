# Generated by Django 4.0.4 on 2022-05-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='img',
            field=models.TextField(default=111),
            preserve_default=False,
        ),
    ]