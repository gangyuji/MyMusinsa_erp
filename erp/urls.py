
 

from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('product/', views.product_list, name='product'),
    path('product-create/', views.product_create, name='product-create'),
    path('inbound/', views.inbound, name='inbound'),
    path('outbound/', views.outbound, name='outbound'),
]