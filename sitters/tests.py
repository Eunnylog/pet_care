import datetime
from django.utils import timezone

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sitters.models import PetSitter
from users.models import User


class SitterCreateTest(APITestCase):

    # def setUp(self):
    #     self.user_data = {
    #         'username': 'testuser',
    #         'email': 'test@testuser.com',
    #         'password': 'passtest'
    #     }
    #     self.sitter_data = {
    #         "title":"날짜 테스트7",
    #         "content":"날짜 테스트7",
    #         "charge":"10000",
    #         "species":1,
    #         "location":1,
    #         "reservation_start":"2023-05-12",
    #         "reservation_end":"2023-05-18"
    #     }
    #     self.user = User.objects.create_user('testuser', 'test@testuser.com', 'passtest')
    #     #왜 여긴
    #     self.access_token = self.client.post(reverse("token_obtain_pair"), self.data).data['access']

    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            'username': 'testuser',
            'email': 'test@testuser.com',
            'password': 'passtest'
        }
        cls.sitter_data = {
            "title":"날짜 테스트7",
            "content":"날짜 테스트7",
            "charge":"10000",
            "species":1,
            "location":1,
            "reservation_start":"2023-05-12",
            "reservation_end":"2023-05-18"
        }
        cls.user = User.objects.create_user('testuser', 'test@testuser.com', 'passtest')

    def setUp(self):
        self.access_token = self.client.post(reverse("token_obtain_pair"), self.data).data['access']

    #로그인이 안된 유저가 post 시도할때 에러
    def test_fail_if_not_logged_in(self):
        url = reverse("PetSitterView")
        response = self.client.post(url, self.sitter_data)
        self.assertEqual(response.status_code, 401)
