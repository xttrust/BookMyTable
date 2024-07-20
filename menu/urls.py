from django.urls import path
from .views import MenuItemListView

urlpatterns = [
    path('list/', MenuItemListView.as_view(), name='menu_item_list'),
]
