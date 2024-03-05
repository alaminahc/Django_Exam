from django.urls import path
from .views import home


# Create your urlpatterns here.
urlpatterns = [
    path('', home, name='home')
]