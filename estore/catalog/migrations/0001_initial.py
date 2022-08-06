# Generated by Django 4.0.4 on 2022-04-24 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['brand_name'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('screen_size', models.FloatField()),
                ('RAM', models.IntegerField()),
                ('hard_disk_size', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.IntegerField(default=0)),
                ('quantity', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Operating_system',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('os_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['os_name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date_time', models.DateTimeField()),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('c', 'Card'), ('b', 'BLIK'), ('t', 'Transfer')], max_length=1)),
                ('delivery_method', models.CharField(choices=[('l', 'Locker'), ('h', 'Home')], max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.client')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('processor_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['processor_name'],
            },
        ),
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.computer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='promocode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.promocode'),
        ),
        migrations.AddField(
            model_name='computer',
            name='os',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.operating_system'),
        ),
        migrations.AddField(
            model_name='computer',
            name='processor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.processor'),
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.cart')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.computer')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.client'),
        ),
    ]
