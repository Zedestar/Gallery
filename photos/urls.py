from django.urls import path
from . import views

# Creating the view here 

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.addPhoto, name='add'),
    path('view/<str:pk>', views.viewPhoto, name='view'),
]