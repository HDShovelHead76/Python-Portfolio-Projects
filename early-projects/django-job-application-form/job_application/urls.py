from django.urls import path
from . import views  # Import views from this app

# App-level URL configuration for job_application
urlpatterns = [
    # Root/homepage → index view
    path("", views.index, name="index"),

    # About page
    path("about/", views.about, name="about"),

    # Contact Us page
    path("contact_us/", views.contact_us, name="contact_us"),
]
