from django.urls import path
from owners import views


urlpatterns = [
    path('', views.PetOwnerView.as_view(), name='petowner_view'),
    path('<int:owner_id>/', views.PetOwnerDetailView.as_view(), name='petowner_detail_View'),
    path('<int:owner_id>/comment/', views.PetOwnerCommentView.as_view(), name='petowner_comment_view'),
    path('<int:owner_id>/comment/<int:comment_id>/', views.PetOwnerCommentDetailView.as_view(), name='petowner_comment_detail_view'),
    path('<int:owner_id>/reservation/', views.SittersForOwnerPRView.as_view(), name='sittersforownerpr_view'),
    path('<int:owner_id>/reservation/<int:user_id>/', views.SitterIsSelectedView.as_view(), name='sitterisselectide_view'),
    path('location/', views.LocationList.as_view(), name='location_list_view'),

]
