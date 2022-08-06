from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('computers/', views.ComputerListView.as_view(), name='computers'),
    path('computer/<int:pk>', views.ComputerDetailView.as_view(), name='computer-detail'),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout', views.logout_request, name= "logout"),
    path('dell_list', views.dell_list, name= "dell_list"),
    path('mac_list', views.mac_list, name= "mac_list"),
    path('lenovo_list', views.lenovo_list, name= "lenovo_list"),
    path('cart/', views.cartdet, name= "cart"),
    path('computer/add_to_cart/<comp_id>', views.add_to_cart, name= "add-to-cart"),
    path('computers/add_to_cart/<comp_id>', views.add_to_cart, name= "add-to-cart"),
    path('cart/delete_from_cart/<comp_id>', views.delete_from_cart, name= "delete-from-cart"),
    path('cart/clear_cart', views.clear_cart, name= "clear-cart"),
    path('cart/update_quantity', views.update_quantity, name= "update-quantity"),
    path('cart/computers/checkout/<cart_id>', views.checkout, name= "checkout"),
    path('computers/search', views.SearchResultsView.as_view(), name='search_results'),
    path('search', views.SearchResultsView.as_view(), name='search_results'),
    path('computers/filter', views.FilterResultsView.as_view(), name='filter_results'),
    path('filter', views.FilterResultsView.as_view(), name='filter_results'),
]

