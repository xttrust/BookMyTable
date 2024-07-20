from django.db import models

class ContactMessage(models.Model):
    """
    Model representing a contact message submitted through the contact form.

    Fields:
        fullname (CharField): Stores the full name of the person contacting.
        email (EmailField): Stores the email address of the person contacting.
        phone (CharField): Stores the phone number of the person contacting (optional).
        message (TextField): Stores the message content submitted by the user.
    """
    
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.fullname}"
