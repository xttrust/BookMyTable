from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'phone', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        if not forms.EmailField().clean(email):
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError('Message is required.')
        if len(message) > 500:
            raise forms.ValidationError('Message cannot be longer than 500 characters.')
        return message

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('Phone number is required.')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone
