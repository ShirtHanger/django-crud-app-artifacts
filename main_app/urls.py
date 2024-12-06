from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('artifacts/', views.artifact_index, name='artifact-index'),
    path('artifacts/<int:artifact_id>/', views.artifact_detail, name='artifact-detail'), # Artifact details, collects by ID.
    # CRUD form logic is handled automatically by Django
    path('artifacts/create/', views.ArtifactCreate.as_view(), name='artifact-create'), # Create a artifact on user end, 
    path('artifacts/<int:pk>/update/', views.ArtifactUpdate.as_view(), name='artifact-update'), # Update
    path('artifacts/<int:pk>/delete/', views.ArtifactDelete.as_view(), name='artifact-delete'), # Delete
    
    # Artifact exhibits route
    path(
    'artifacts/<int:artifact_id>/add-exhibit/', 
    views.add_exhibit, 
    name='add-exhibit'
    ),
    
    # Sign up route
    path('accounts/signup/', views.signup, name='signup'),
]
