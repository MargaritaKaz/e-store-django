from django.http import HttpResponse
from .models import Brand, Operating_system, Processor, Promocode, Computer, Order, Manager, OrderDetail, Cart, CartDetail, CartItem, Order_status
from django.shortcuts import render, redirect
from django.views import generic
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging


def index(request):
    """View function for home page of site."""
    computers = Computer.objects.filter(~Q(discount=0))
    context = {
        'computer_list': computers,
    }
    return render(request, 'index.html', context=context)


def dell_list(request):
    computers = Computer.objects.all().filter(brand=3)
    context = {
        'computer_list': computers,
    }
    return render(request, template_name="catalog/computer_list.html", context=context)

def mac_list(request):
    computers = Computer.objects.all().filter(brand=4)
    context = {
        'computer_list': computers,
    }
    return render(request, template_name="catalog/computer_list.html", context=context)

def lenovo_list(request):
    computers = Computer.objects.all().filter(brand=1)
    context = {
        'computer_list': computers,
    }
    return render(request, template_name="catalog/computer_list.html", context=context)

class ComputerDetailView(generic.DetailView):
    model = Computer

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, template_name="catalog/register.html", context={"register_form": form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request, template_name="catalog/login.html", context={"login_form": form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("index")


class ComputerListView(generic.ListView):
	paginate_by = 25
	model = Computer
	context_object_name = 'computer_list'

def cartdet(request):
	if request.user.is_authenticated:
		try:
			carto = Cart.objects.get(user=request.user)
		except Cart.DoesNotExist:
			carto = Cart(user = request.user)
			carto.save()
		cart_items = CartItem.objects.all().filter(cart=carto)
		subtotal = 0
		quantity = 0
		for item in cart_items:
			subtotal+=item.product.newprice*item.quantity
			quantity+=item.quantity
		context = {
			'cart_id' : carto.auto_increment_id,
			'user_cart': cart_items,
			'subtotal' : subtotal,
			'quantity' : quantity
		}
		return render(request, 'catalog/cart.html', context=context)
	else:
		messages.error(request, "You are not logged in")
		return redirect("index")


def add_to_cart(request, comp_id):
	if request.user.is_authenticated:
		comp = Computer.objects.get(auto_increment_id=comp_id)
		try:
			cart = Cart.objects.get(user=request.user)
		except Cart.DoesNotExist:
			cart = Cart(user = request.user)
			cart.save()
		try:
			obj = CartItem.objects.filter(cart=cart).get(product=comp)
			obj.quantity=obj.quantity + 1
			obj.save()
		except CartItem.DoesNotExist:
			obj = CartItem(product=comp, quantity=1, cart=cart)
			obj.save()
		messages.info(request, "You have successfully added item to cart")
		return redirect("index")
	else:
		messages.error(request,"You are not logged in")
		return redirect("index")

def delete_from_cart(request, comp_id):
	comp = Computer.objects.get(auto_increment_id=comp_id)
	cart = Cart.objects.get(user=request.user)
	CartItem.objects.filter(cart=cart).get(product=comp).delete()
	messages.info(request, "You deleted item from cart")
	return redirect("cart")

def clear_cart(request):
	cart = Cart.objects.get(user=request.user)
	CartItem.objects.filter(cart=cart).all().delete()
	messages.info(request, "You deleted all items from cart")
	return redirect("cart")

def checkout(request, cart_id):
	curr_date = datetime.now()
	ordet_status = Order_status.objects.get(auto_increment_id = 1)
	user_cart = Cart.objects.get(auto_increment_id = cart_id)
	cart_items = CartItem.objects.filter(cart=user_cart)
	new_order = Order(order_date_time = curr_date, total_sum = 0, order_status = ordet_status, client = request.user)
	new_order.save()
	for items in cart_items:
		odet = OrderDetail(order = new_order, computer = items.product, quantity = items.quantity)
		odet.save()
		new_order.total_sum += items.product.newprice*items.product.quantity
		new_order.save()
		prod = items.product
		prod.quantity -= items.quantity
		prod.save()
		items.delete()
	messages.info(request, "Your order is submitted")	
	return redirect("cart")

class SearchResultsView(ListView):
	model = Computer
	template_name = 'index'
	context_object_name = 'computer_list'
	#prod=Product.objects.all()

	def get_queryset(self):
		query = self.request.GET.get('search')
		products=Computer.objects.filter(Q(title__icontains=query))
		return products


class FilterResultsView(ListView):
	model = Computer
	template_name = 'index'
	context_object_name = 'computer_list'

	def get_queryset(self):
		form_brand = self.request.GET.get('brand')
		form_OS = self.request.GET.get('OS')
		form_RAM = self.request.GET.get('RAM')
		form_startprice = self.request.GET.get('startprice')
		form_endprice = self.request.GET.get('endprice')
		products = Computer.objects.all()

		if form_brand != 'All':
			data_brand = Brand.objects.get(brand_name=form_brand)
			products = products.filter(brand=data_brand)
		if form_OS != 'All':
			data_OS = Operating_system.objects.get(os_name=form_OS)
			products = products.filter(os=data_OS)
		if form_RAM != 'All':
			products = products.filter(RAM=form_RAM)
		if form_startprice != '0':
			products = products.filter(price__gte = form_startprice)
		if form_startprice != '10000':
			products = products.filter(price__lte = form_endprice)
		return products

def update_quantity(request):
	quant = request.POST.get('quant_id')
	prod_id = request.POST.get('item_id')
	user_cart = Cart.objects.get(user=request.user)
	product = Computer.objects.get(auto_increment_id=prod_id)
	cart_item = CartItem.objects.get(product=product)
	cart_item.quantity = quant
	cart_item.save()
	return redirect("cart")		