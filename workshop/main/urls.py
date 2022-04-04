from django.urls import path

from workshop.main.views.generic import HomeView, DashboardView
from workshop.main.views.pet_photos import CreatePetPhotoView, like_pet_photo, \
    PetPhotoDetailsView, EditPetPhotoView
from workshop.main.views.pets import CreatePetView, EditPetView, DeletePetView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('photo/add/', CreatePetPhotoView.as_view(), name='create pet photo'),
    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),
)
