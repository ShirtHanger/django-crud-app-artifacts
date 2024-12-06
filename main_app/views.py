from django.shortcuts import render, redirect
# Import login functionality
from django.contrib.auth.views import LoginView
# Import Class Based View CRUD stuff
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# For login-signup stuff
from django.views.generic import ListView, DetailView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# For login protected routes
from django.contrib.auth.decorators import login_required 
# Import the mixin for class-based view protection
from django.contrib.auth.mixins import LoginRequiredMixin

# Import Artifact Model
from .models import Artifact
# Import form for new exhibits for artifact
from .forms import ExhibitForm

# Create your views here.

# Import HttpResponse to send text-based responses
# Obeslete when you make a proper home page
from django.http import HttpResponse

# Define the home view function
class Home(LoginView):
    # Returns main_app/templates/home.html
    template_name = 'home.html'

# Now let's define an about page
def about(request):
    # Returns html file from main_app/templates/about.html
    return render(request, 'about.html')

# INDEX PAGE
""" 
def artifact_index(request): # Shows ALL artifacts in database
    # Render the artifacts/index.html template with the artifacts data
    # Turns it into a dictionary with a single key, 'artifacts'
    artifacts = Artifact.objects.all()  # look familiar?
    return render(request, 'artifacts/index.html', {'artifacts': artifacts})
 """

@login_required
def artifact_index(request): # Shows just the logged user's artifacts
    artifacts = Artifact.objects.filter(user=request.user)
    # You could also retrieve the logged in user's artifacts like this
    # artifacts = request.user.artifact_set.all()
    return render(request, 'artifacts/index.html', { 'artifacts': artifacts })

# SHOW PAGE
@login_required
def artifact_detail(request, artifact_id): # Grabs a specific artifact by Django ID
    artifact = Artifact.objects.get(id=artifact_id)
    
    # instantiate ExhibitForm to be rendered in the template
    exhibit_form = ExhibitForm()
    
    # Return both singular artifact and all exhibits associated with singular artifact
    return render(request, 'artifacts/detail.html', {
        # include the artifact and exhibit_form in the context
        'artifact': artifact, 'exhibit_form': exhibit_form
    })
    
# ADD A EXHIBIT METHOD
@login_required
def add_exhibit(request, artifact_id):
    # create a ModelForm instance using the data in request.POST
    form = ExhibitForm(request.POST) # Captures exhibit data, preps for database
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the artifact_id assigned
        new_exhibit = form.save(commit=False)
        new_exhibit.artifact_id = artifact_id
        new_exhibit.save()
    return redirect('artifact-detail', artifact_id=artifact_id)


# SIGN UP FUNCTIONALITY
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in and redirect them
            login(request, user)
            return redirect('artifact-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
    # In Javascript




""" These will automatically handle CRUD form logic! """
class ArtifactCreate(LoginRequiredMixin, CreateView):
    model = Artifact
    # fields = '__all__' # Shows form of all properties, including owned user
    # This works too but above is more efficient...
    # But since there are users, we need to hide the "User" property
    fields = ['name', 'culture', 'description', 'year_discovered']
    
    # This inherited method is called when a
    # valid artifact form is being submitted
    def form_valid(self, form):
        # Automatically assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the artifact
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class ArtifactUpdate(LoginRequiredMixin, UpdateView):
    model = Artifact
    # Disallow renaming of a artifact by excluding the name field!
    fields = ['culture', 'description', 'year_discovered']

class ArtifactDelete(LoginRequiredMixin, DeleteView):
    model = Artifact
    success_url = '/artifacts/'