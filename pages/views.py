from django.http import Http404
from django.shortcuts import render,get_object_or_404

from .models import Product,Delivery
# Create your views here.

def index(request):
    return render(request,'pages/index.html',{'pro':Product.objects.all()})
def  cart(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        PhoneNumber = request.POST.get('PhoneNumber')
        YourAddress = request.POST.get('YourAddress')
        items = request.POST.get('items')
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        details = request.POST.get('details')
        data = Delivery(FirstName = FirstName,LastName=LastName,PhoneNumber=PhoneNumber,YourAddress=YourAddress,items=items,quantity=quantity,size=size ,details=details)
        data.save()
    return render(request,'pages/cart.html',{'pro':Product.objects.all()})
def returns(request):
    return render(request,'pages/returns.html')

