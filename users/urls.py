from django.urls import path,include
from users import views

urlpatterns = [
    path('<int:user_id>/owner-review/', views.PetOwnerReviewView.as_view(),name='petownerreview_view'),
    path('<int:user_id>/sitter-review/', views.PetSitterReviewView.as_view(),name='petsitterreview_view'),
    path('<int:user_id>/owner-review/<int:review_id>/', views.PetOwnerReviewDetailView.as_view(),name='petownerreview_view'),
    path('<int:user_id>/sitter-review/<int:review_id>/', views.PetSitterReviewDetailView.as_view(),name='petsitterreview_view'),
    path('<int:user_id>/star-rating/', views.StarRatingView.as_view(), name = 'starrating_view'),
]