# Generated by Django 4.0.4 on 2022-05-20 08:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_order_promocode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='client',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_sum',
        ),
        migrations.RemoveField(
            model_name='cartdetail',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartdetail',
            name='computer',
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='catalog.client'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price_ht', models.FloatField(blank=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.computer')),
            ],
        ),
    ]