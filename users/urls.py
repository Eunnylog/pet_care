from django.urls import path,include
from users import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='sign_up'),
    path('sign/',views.UserView.as_view(),name='sign_up'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('<int:user_id>/owner-review/', views.PetOwnerReviewView.as_view(),name='petownerreview_view'),
    path('<int:user_id>/sitter-review/', views.PetSitterReviewView.as_view(),name='petsitterreview_view'),
    path('<int:user_id>/owner-review/<int:review_id>/', views.PetOwnerReviewDetailView.as_view(),name='petownerreview_view'),
    path('<int:user_id>/sitter-review/<int:review_id>/', views.PetSitterReviewDetailView.as_view(),name='petsitterreview_view'),
    path('<int:user_id>/star-rating/', views.StarRatingView.as_view(), name = 'starrating_view'),
]