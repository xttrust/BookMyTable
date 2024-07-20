from django.apps import AppConfig

class ContactConfig(AppConfig):
    """
    Configuration class for the Contact application.

    This class contains configuration settings for the Contact app,
    including the default primary key field type and the app's name.
    """
    
    # Specify the default auto field type to use for primary keys in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the application, used by Django to reference this app
    name = 'contact'
