from django.shortcuts import render
from product.models import Item
from django.core.paginator import Paginator
# Create your views here.
def core(request):
    product_list = Item.objects.all()
    paginator = Paginator(product_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'product':page_obj}
    return render(request,'core/store.html',context)