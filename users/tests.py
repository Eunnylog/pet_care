from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User

# class ReviewCreateTest(APITestCase):
#     def setUp(self):
#         self.review_data = {'contet':'테스트','star':5}
#         self.user = User.objects.create_user('hello','hello@hi.com','hello')
        
#     def test_create_review(self):
#         response = self.client.post(
#             path = reverse("petownerreview_view", kwargs={"user_id":1}),
#             data = self.review_data,
#         )
#         self.assertEqual(response.status_code, 201)