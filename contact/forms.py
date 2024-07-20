from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """
    A form for users to send contact messages. It includes fields for full name, email, phone number, and message.
    
    This form is linked to the ContactMessage model and includes validation logic for each field.
    """
    
    class Meta:
        """
        Meta information for the form. Specifies the model and fields to include in the form.
        """
        model = ContactMessage
        fields = ['fullname', 'email', 'phone', 'message']

    def clean_email(self):
        """
        Validates the email field.

        Checks if the email is provided and if it is in a valid format.

        Returns:
            str: The cleaned email address if valid.
        
        Raises:
            forms.ValidationError: If the email is not provided or not valid.
        """
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        if not forms.EmailField().clean(email):
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def clean_message(self):
        """
        Validates the message field.

        Checks if the message is provided and if it does not exceed 500 characters.

        Returns:
            str: The cleaned message if valid.
        
        Raises:
            forms.ValidationError: If the message is not provided or exceeds 500 characters.
        """
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError('Message is required.')
        if len(message) > 500:
            raise forms.ValidationError('Message cannot be longer than 500 characters.')
        return message

    def clean_phone(self):
        """
        Validates the phone field.

        Checks if the phone number is provided and contains only digits.

        Returns:
            str: The cleaned phone number if valid.
        
        Raises:
            forms.ValidationError: If the phone number is not provided or contains non-digit characters.
        """
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('Phone number is required.')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone
