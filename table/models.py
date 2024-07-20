from django.db import models

class Table(models.Model):
    """
    Model representing a table in the restaurant.

    Fields:
        number (IntegerField): The number identifier for the table.
        seats (IntegerField): The number of seats at the table, with a default value of 6.
    """
    
    # Field to store the table number
    number = models.IntegerField()
    
    # Field to store the number of seats at the table, defaulting to 6
    seats = models.IntegerField(default=6)

    def __str__(self):
        """
        Return a string representation of the Table instance.
        
        Returns:
            str: A string indicating the table number.
        """
        return f"Table {self.number}"
