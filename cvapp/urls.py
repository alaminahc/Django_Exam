from django.urls import path
from .views import cvcreate, cvview, delcvprofile, cvupdate


# Create your urlpatterns here.
urlpatterns = [
    path('cvcreate/', cvcreate, name='cvcreate'),
    path('cvview/', cvview, name='cvview'),
    path('delcvprofile/<int:id>/', delcvprofile, name='delcvprofile'),
    path('cvupdate/<int:id>/', cvupdate, name='cvupdate'),
    # path('pdfview/', pdfview, name='pdfview'),
    
]
