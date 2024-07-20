from django.db import models

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.fullname}"