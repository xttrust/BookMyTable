from django.views.generic import TemplateView
from menu.models import MenuCategory, MenuItem

class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch all categories
        categories = MenuCategory.objects.all()
        
        # Create a list of tuples (category, menu_items)
        menu_items_by_category = [(category, MenuItem.objects.filter(category=category)) for category in categories]
        
        context['menu_items_by_category'] = menu_items_by_category
        
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class MenuPageView(TemplateView):
    template_name = 'pages/menu.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
