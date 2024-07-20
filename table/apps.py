from django.apps import AppConfig

class TableConfig(AppConfig):
    """
    Configuration class for the Table app in the Django project.

    Attributes:
        default_auto_field (str): Specifies the default field type to use for primary keys
        name (str): The name of the application, used by Django to reference this app
    """
    
    # Specify the default auto field type to use for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the application, used by Django to reference the app
    name = 'table'
