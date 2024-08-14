from django.urls import path
from . import views


urlpatterns = [
    path('', views.synonyms_view, name='synonyms')
]