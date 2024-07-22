from django.core.paginator import Paginator
from django.utils.text import slugify
from django.views.generic import TemplateView
from .models import MenuCategory, MenuItem


class MenuItemListView(TemplateView):
    """
    View for listing menu items with pagination and tabbed display.

    Attributes:
        template_name (str): The template to be used for rendering the menu
        items.
    """
    template_name = 'menu/menu_item_list.html'

    def get_context_data(self, **kwargs):
        """
        Returns the context data for rendering the menu items.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: Context data including paginated menu items categorized
            by their category.
        """
        context = super().get_context_data(**kwargs)
        categories = MenuCategory.objects.all()

        menu_items_by_category = []
        for category in categories:
            items = MenuItem.objects.filter(category=category)
            paginator = Paginator(items, 9)
            page_number = self.request.GET.get(
                f'{slugify(category.name)}_page', 1)
            page_obj = paginator.get_page(page_number)
            menu_items_by_category.append((category, page_obj))

        context['menu_items_by_category'] = menu_items_by_category
        return context
