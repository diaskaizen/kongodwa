from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'store'

urlpatterns = [
    #path('customer/<str:pk_test>/', views.customer, name="customer"),

    #path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    #path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    #path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    #path('base/', views.base, name="base"),
    path('product/<int:product_id>/', views.detail, name="detail"),

]
