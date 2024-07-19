from django.db import models

class Table(models.Model):
    number = models.IntegerField()
    seats = models.IntegerField(default=6)

    def __str__(self):
        return f"Table {self.number}"
