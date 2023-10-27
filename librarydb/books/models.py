from django.db import models
from django.urls import reverse
# Create your models here.

class Books(models.Model):
    titel = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    erscheinungsjahr = models.CharField(max_length=100)
    verlag = models.CharField(max_length=100)

    def __str__(self):
        return self.titel
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])