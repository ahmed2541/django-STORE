from urllib import request
from django.shortcuts import render,redirect
from django.urls import reverse
from product.forms import AddItem
from .models import Item
from django.core.paginator import Paginator
# Create your views here.
def item(request):
    product_list = Item.objects.all()
    paginator = Paginator(product_list,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # paginator = paginator+Paginator(product_list,3)
    context = {'product':page_obj,}
    return render(request,'product/products.html',context)





def product_detail(request,slug):
    product_detail = Item.objects.get(slug=slug)
    context = {'product':product_detail}
    return render(request,'product/products_detail.html',context)



def add_item(request):

    if request.method=='POST':
        form = AddItem(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:product'))

    else :
        form = AddItem()

    context = {'form':form}
    return render(request,'product/add_product.html',context)    