from django.urls import path
from . import views
urlpatterns = [
	path("", views.index, name="index"),
	path("Jesoah", views.Jesoah, name="Jesoah"),
	path("Mithr", views.Mithr, name="Mithr"),
	path("<str:name>", views.greet, name="greet")]