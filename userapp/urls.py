from django.urls import path
from .views import signup, signin, signout, verify_acco, change_pass



# Create your urlpatterns here.
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('verify_acco/', verify_acco, name= 'verify_acco'),
    path('change_pass/', change_pass, name= 'change_pass'),

]