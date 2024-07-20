from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    """
    Handles the contact form view. Processes form submissions and renders the contact page.
    
    If the request method is POST, it processes the submitted form data:
    - Validates the form
    - Saves the form data if valid
    - Displays a success message and redirects the user
    
    If the request method is GET, it initializes an empty form for the user to fill out.
    
    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.
    
    Returns:
        HttpResponse: Renders the contact page template with the form.
    """
    # Check if the request method is POST
    if request.method == 'POST':
        # Instantiate the ContactForm with POST data
        form = ContactForm(request.POST)
        
        # Validate the form data
        if form.is_valid():
            # Save the form data if valid
            form.save()
            # Add a success message to be displayed to the user
            messages.success(request, 'Your message has been sent successfully.')
            # Redirect to the contact page after successful submission
            return redirect('contact')
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Please correct the errors below.')
    else:
        # Instantiate an empty ContactForm for GET requests
        form = ContactForm()

    # Render the contact page with the form
    return render(request, 'contact/contact.html', {'form': form})
