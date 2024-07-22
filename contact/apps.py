from django.apps import AppConfig


class ContactConfig(AppConfig):

    # Specify the default auto field type to use for primary keys in this app
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the application, used by Django to reference this app
    name = 'contact'
