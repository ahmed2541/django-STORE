from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [ 
    path('',views.item,name='product'),
    path('product/<str:slug>/',views.product_detail,name='product_detail'),
    path('add/',views.add_item,name='add_product'),

]