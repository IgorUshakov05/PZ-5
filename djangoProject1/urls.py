from django.urls import path
from PRFive import views

urlpatterns = [
    path('', views.index, name='index'),  # This maps the root URL to the index view
path('items/', views.tovars, name='tovar'),  # This maps the root URL to the index view
path('trainers/', views.trainers, name='trainers'),  # This maps the root URL to the index view

]
