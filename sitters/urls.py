from django.urls import path, include
from sitters import views


urlpatterns = [
    path('', views.sitter_view, name="sitter_view"),
]