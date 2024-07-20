from django.shortcuts import render
from .models import Table

def table_list(request):
    """
    Retrieves and displays a list of all tables in the restaurant.

    Fetches all Table objects from the database and renders them in the 'table/table_list.html' template.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: Renders the table list template with the context containing all Table objects.
    """
    # Retrieve all Table objects from the database
    tables = Table.objects.all()
    
    # Render the 'table/table_list.html' template with the list of tables
    return render(request, 'table/table_list.html', {'tables': tables})
