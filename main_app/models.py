from django.db import models
from django.urls import reverse

# Create your models here.

class Artifact(models.Model): #References model class, new API schema!
    name = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    description = models.TextField(max_length=1000) # textField is better for longer text fields
    year_discovered = models.IntegerField()
    
    # Override class object nonsense, just return the artifact's name
    def __str__(self):
        return self.name
    
    # Method to acquirred URL for a particular artifact instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL
        return reverse('artifact-detail', kwargs={'artifact_id': self.id})