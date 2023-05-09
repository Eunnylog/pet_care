from django.urls import path
from owners import views


urlpatterns = [
    path('', views.PetOwnerView.as_view(), name='PetOwner_View')
]