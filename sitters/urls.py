from django.urls import path
from sitters import views


urlpatterns = [
    path('', views.PetSitterView.as_view(), name='PetSitterView'),
    path('<int:sitter_id/', views.PetSitterDetailAPI.as_view(), name='PetSitterDetailAPI'),
]