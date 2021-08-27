from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('', views.signup, name="signup"),
    path('', views.contact, name="contact"),
    path('', views.about, name="about"),
    path('', views.projects, name="projects"),
    path('', views.homepage, name="homepage"),   
]

