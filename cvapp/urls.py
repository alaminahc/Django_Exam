from django.urls import path
from . import views


# Create your urlpatterns here.
urlpatterns = [
    path('cvcreate/', views.cvcreate, name='cvcreate'),
    path('cvview/', views.cvview, name='cvview'),
    path('delcvprofile/<int:id>/', views.delcvprofile, name='delcvprofile'),
    path('cvupdate/<int:id>/', views.cvupdate, name='cvupdate'),
    path('cv/download/<int:cv_id>/', views.cv_download, name='cv_pdf'),

    
]
