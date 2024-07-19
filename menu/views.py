from django.shortcuts import render
from .models import MenuItem

def menu_item_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_item_list.html', {'items': items})
