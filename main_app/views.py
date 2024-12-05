from django.shortcuts import render

# Import Class Based View CRUD stuff
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# The Artifact Model
from .models import Artifact

# Create your views here.

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')


# Now let's define an about page
def about(request):
    # Returns html file from main_app/templates/about.html
    return render(request, 'about.html')

# INDEX PAGE
def artifact_index(request):
    # Render the artifacts/index.html template with the artifacts data
    # Turns it into a dictionary with a single key, 'artifacts'
    artifacts = Artifact.objects.all()  # look familiar?
    return render(request, 'artifacts/index.html', {'artifacts': artifacts})

# SHOW PAGE
def artifact_detail(request, artifact_id): # Grabs a specific artifact by Django ID
    artifact = Artifact.objects.get(id=artifact_id)
    return render(request, 'artifacts/detail.html', {'artifact': artifact})



""" THese will automatically handle CRUD form logic! """
class ArtifactCreate(CreateView):
    model = Artifact
    fields = '__all__' # Shows form of all properties
    # This works too but above is more efficient.
    # fields = ['name', 'culture', 'description', 'year_discovered']
    
class ArtifactUpdate(UpdateView):
    model = Artifact
    # Disallow renaming of a artifact by excluding the name field!
    fields = ['culture', 'description', 'year_discovered']

class ArtifactDelete(DeleteView):
    model = Artifact
    success_url = '/artifacts/'