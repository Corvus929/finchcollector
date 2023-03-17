from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.

class Finch(models.Model):
    subspecies = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    lifespan = models.IntegerField()
    def __str__(self):
        return self.subspecies
    def get_absolute_url(self): 
        return reverse('detail', kwargs={'finch.id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']
