from django.views.generic import ListView
from .models import MenuCategory, MenuItem

class MenuItemListView(ListView):
    """
    View for listing all menu items.

    Attributes:
        model (Model): The model to use for retrieving menu items.
        template_name (str): The template to be used for rendering the menu items.
        context_object_name (str): The name of the context variable to be used in the template.
    """
    template_name = 'menu/menu_item_list.html'
    context_object_name = 'menu_items_by_category'

    def get_queryset(self):
        categories = MenuCategory.objects.all()
        menu_items_by_category = [
            (category, MenuItem.objects.filter(category=category)[:9])  # Limit to 9 items
            for category in categories
        ]
        return menu_items_by_category
