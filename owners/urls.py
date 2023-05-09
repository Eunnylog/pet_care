from django.urls import path
from owners import views


urlpatterns = [
    path('', views.PetOwnerView.as_view(), name='petowner_view'),
    path('<int:owner_id>/', views.PetOwnerDetailView.as_view(), name='petowner_detail_View'),
    path('<int:owner_id>/comment/', views.PetOwnerCommentView.as_view(), name='comment_view'),
    path('<int:owner_id>/comment/<int:comment_id>/', views.PetOwnerCommentDetailView.as_view(), name='comment_detail_view'),

]
