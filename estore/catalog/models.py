from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# managers to manage orders, registration.
# filter, categories
#


class Brand(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['brand_name']

    def __str__(self):
        return f'{self.auto_increment_id} ({self.brand_name})'


class Operating_system(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    os_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['os_name']

    def __str__(self):
        return self.os_name


class Processor(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    processor_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['processor_name']

    def __str__(self):
        return self.processor_name


class Promocode(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    discount = models.IntegerField()

    def __str__(self):
        return self.code


class Computer(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    screen_size = models.FloatField()
    RAM = models.IntegerField()
    hard_disk_size = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.IntegerField(default=0)
    newprice = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    img = models.TextField()
    # relationships
    brand = models.ForeignKey('Brand', on_delete=models.RESTRICT)
    os = models.ForeignKey('Operating_system', on_delete=models.RESTRICT)
    processor = models.ForeignKey('Processor', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['auto_increment_id']

    def __str__(self):
        return f'{self.auto_increment_id} ({self.title})'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this comp."""
        return reverse('computer-detail', args=[str(self.auto_increment_id)])

class Order_status(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.auto_increment_id} ({self.status_name})'

class Order(models.Model):
    # status
    auto_increment_id = models.AutoField(primary_key=True)
    order_date_time = models.DateTimeField()
    total_sum = models.DecimalField(decimal_places=2, max_digits=10)

    # PAYMENT_METHOD = (
    #     ('c', 'Card'),
    #     ('b', 'BLIK'),
    #     ('t', 'Transfer'),
    # )
    # payment_method = models.CharField(
    #     max_length=1,
    #     choices=PAYMENT_METHOD,
    # )

    # DELIVERY_METHOD = (
    #     ('l', 'Locker'),
    #     ('h', 'Home'),
    # )
    # delivery_method = models.CharField(
    #     max_length=1,
    #     choices=DELIVERY_METHOD,
    # )
    # relations
    order_status = models.ForeignKey(Order_status, on_delete=models.RESTRICT)
    client = models.ForeignKey(User, on_delete=models.RESTRICT)
    # manager = models.ForeignKey('Manager', on_delete=models.RESTRICT)
    # promocode = models.ForeignKey('Promocode', on_delete=models.RESTRICT, default='None')

    def __str__(self):
        return f'{self.auto_increment_id} ({self.client.username})'


class Manager(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    computer = models.ForeignKey(Computer, on_delete=models.RESTRICT)
    quantity = models.IntegerField()

    def __str__(self):
        return f'order num {self.order.auto_increment_id} ({self.order.client.username})'


class CartDetail(models.Model):
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # computer = models.ForeignKey(Computer, on_delete=models.RESTRICT)
    quantity = models.IntegerField()


# new cart
class Cart(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this comp."""
        return reverse('cart-detail', args=[str(self.auto_increment_id)])

    def __str__(self):
        return f'{self.user.username} cart'


class CartItem(models.Model):
    product = models.ForeignKey(Computer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def __str__(self):
        return self.cart.user.username + " - " + self.product.title
