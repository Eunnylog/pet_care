from django.urls import path
from sitters import views


urlpatterns = [
    path('', views.PetSitterView.as_view(), name='PetSitterView'),
    path('<int:sitter_id/', views.PetSitterDetailAPI.as_view(), name='PetSitterDetailAPI'),
    
    
    # path('<int:sitter_id>/comment/', views.PetSitterCommentView.as_view(), name='petsitter_comment_view'),
    # path('<int:sitter_id>/comment/<int:comment_id>/', views.PetSitterCommentDetailView.as_view(), name='petsitter_comment_detail_view'),
]