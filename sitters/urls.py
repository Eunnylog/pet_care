from django.urls import path, include
from sitters import views


urlpatterns = [
    path('', views.sitter_view, name="sitter_view"),
    
    
    # path('<int:sitter_id>/comment/', views.PetSitterCommentView.as_view(), name='petsitter_comment_view'),
    # path('<int:sitter_id>/comment/<int:comment_id>/', views.PetSitterCommentDetailView.as_view(), name='petsitter_comment_detail_view'),
]