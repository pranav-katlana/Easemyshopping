from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobile , Gadgets 
 
def home(request):
    return render(request, 'home.html')

def product(request):
    item = Mobile.objects.all()
    return render(request, 'product.html', {"items":item})
 

def productview(request , myid, price):
    item = Mobile.objects.filter(id=myid)
    data = [item]
    cashback1 = 0.03*price
    cashback1 = format(cashback1 , ".2f")
    cashback2 = 0.02*price
    cashback2 = format(cashback2 , ".2f")

    database = {"items":item[0] ,"cashbacks1":cashback1, "cashbacks2":cashback2}
    return render(request, 'productview.html', database )


def orderforme(request, myid):
    item = Mobile.objects.filter(id=myid)
    return render(request, 'orderforme.html' , {"items":item[0]})

def gadgets(request):
    item = Gadgets.objects.all()
    database =  {"items": item}
    return render(request , 'gadgets.html', database)

def cashbackform(request):
    return render(request, "cashbackform.html")

def gadgetsview(request):
    return render(request, 'gadgetsview.html')