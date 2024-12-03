from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')


# Now let's define an about page
def about(request):
    # Returns html file from main_app/templates/about.html
    return render(request, 'about.html')

class Artifact:
    def __init__(self, name, culture, description, year_discovered):
        self.name = name
        self.culture = culture
        self.description = description
        self.year_discovered = year_discovered

# Create a list of Artifact instances
artifacts = [
    Artifact("Rosetta Stone", "Ancient Egyptian", "A granodiorite stele inscribed with three scripts: Greek, Demotic, and Hieroglyphic.", 1799),
    Artifact("Terracotta Army", "Ancient Chinese", "A collection of terracotta sculptures depicting the armies of Qin Shi Huang, the first Emperor of China.", 1974),
    Artifact("Venus de Milo", "Ancient Greek", "An ancient Greek statue representing Aphrodite, the goddess of love and beauty.", 1820),
    Artifact("Dead Sea Scrolls", "Ancient Jewish", "A collection of Jewish texts found in the Qumran Caves, significant for biblical history.", 1947),
    Artifact("Mask of Tutankhamun", "Ancient Egyptian", "The funerary mask of the young Pharaoh Tutankhamun, made of gold and gemstones.", 1922)
]

def artifact_index(request):
    # Render the artifacts/index.html template with the artifacts data
    return render(request, 'artifacts/index.html', {'artifacts': artifacts})