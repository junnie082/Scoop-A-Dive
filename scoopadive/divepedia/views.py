from django.shortcuts import render
from divepedia.api import check_jeju_shops
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request, 'divepedia/dive_shops.html')

def view_jeju_shops(request):
    shops = check_jeju_shops()
    print("VIew JEJU!s")
    return render(request, 'divepedia/jeju_dive_shops.html', {"shops": shops})