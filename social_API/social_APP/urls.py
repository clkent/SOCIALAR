from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'geo/$', views.ListGeoData.as_view()),
]