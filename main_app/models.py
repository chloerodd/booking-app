from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    details = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        
        
class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review by {self.name} - Rating: {self.rating}'