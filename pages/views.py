from django.views.generic import TemplateView
from menu.models import MenuCategory, MenuItem

from django.views.generic import TemplateView
from menu.models import MenuCategory, MenuItem


class HomePageView(TemplateView):
    """
    View for the home page. Inherits from TemplateView.

    Attributes:
        template_name (str): The template to be used for rendering
        the home page.
    """
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        """
        Returns the context data for rendering the home page.

        Args:
            **kwargs: Additional keyword arguments passed to the method.

        Returns:
            dict: Context data including menu items categorized by
            their category, limited to 9 items per category.
        """
        # Retrieve the base context data from the parent class
        context = super().get_context_data(**kwargs)

        # Fetch all menu categories from the database
        categories = MenuCategory.objects.all()

        # Create a list of tuples where each tuple contains a
        # category and its corresponding menu items

        # Limit the number of menu items per category to 9
        menu_items_by_category = [
            (category, MenuItem.objects.filter(category=category)[:9])
            for category in categories
        ]

        # Add the categorized menu items to the context data
        context['menu_items_by_category'] = menu_items_by_category

        return context
