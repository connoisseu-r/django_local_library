from django.db import models

# Create your models here.
class Day(models.Model):
    day = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string represent the day of the week."""
        return self.day


class Plan(models.Model):
    """Plan of day's meal"""
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    meal = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meal
