from django.urls import path
from .views import analyze_location

urlpatterns = [
    path('analyze/<str:location>/', analyze_location, name='analyze-location'),
]