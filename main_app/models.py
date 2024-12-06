from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

# Import the default User model
from django.contrib.auth.models import User

# A tuple of 2-tuples added above our models
PLANETS = (
    ('E', 'Great African Museum of Earth - Zimbabwe'),
    ('M', 'Martian Colony - Russian Frontier'),
    ('P', 'Pluto Stronghold - Chinese Spaceways')
)

class Artifact(models.Model): #References model class, new API schema!
    name = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    description = models.TextField(max_length=1000) # textField is better for longer text fields
    year_discovered = models.IntegerField()
    
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Override class object nonsense, just return the artifact's name
    def __str__(self):
        return self.name
    
    # Method to acquirred URL for a particular artifact instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL
        return reverse('artifact-detail', kwargs={'artifact_id': self.id})
    
    
# Artifacts have many exhibits
class Exhibit(models.Model):
    # The first optional positional argument overrides the label
    date = models.DateField('Exhibit date')
    planet = models.CharField( # Earth, Pluto, or Mars (EPM)
        max_length=1, 
        # add the 'choices' field option from the PLANETS tuple
        choices=PLANETS,
        # set the default value for planet to be Earth (E) by accessing tuple index
        default=PLANETS[0][0]
    )
    
    # Add foreign key for the artifact this exhibit belongs to
    # Create a artifact_id column for each exhibit in the database
    
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE) 
    # This function will prevent the database from rolling into itself if you delete a artifact that has exhibits, 
    # it deletes the exhibits too
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        # return f"{self.get_meal_display()} on {self.date}"
        return f"{self.get_planet_display()} on {self.date}"
    
    # Define default order of exhibits
    class Meta:
        ordering = ['-date']  # Newest exhibits appear first