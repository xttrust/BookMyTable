from django.urls import path
from .views import menu_item_list

urlpatterns = [
    path('list/', menu_item_list, name='menu_item_list'),
]
