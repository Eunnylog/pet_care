from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from owners.models import PetOwner, Location, Species
from users.models import User
import csv


# 오너 게시글 작성 테스트
class OwnerCreateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {"username": "test1","email":"test1@test.com", "password":"1234"}
        cls.owner_post_data = {
            "title": "테스트 게시글",
            "content": "테스트 합니다",
            "location": 1,
            "charge": "5000",
            "species": 1,
            "reservation_start": "2023-05-20",
            "reservation_end": "2023-05-30"
        }
        cls.user = User.objects.create_user("test1","test1@test.com","1234")
        
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']

        with open('./location_code.csv', newline='', encoding='UTF8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                print(row)
                Location.objects.create(
                    city=row['city'],
                    state=row['state']
                )

        with open('./species_breeds.csv', newline='', encoding='UTF8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                print(row)
                Species.objects.create(
                    species=row['species'],
                    breeds=row['breeds']
                )
    
    # 로그인하지 않은 유저 접근 시 에러 작동 확인    
    def test_fail_if_not_logged_int(self):
        url = reverse('petowner_view')
        response = self.client.post(url, self.owner_post_data)
        self.assertEqual(response.status_code, 401)
    
    # 게시글 작성
    def test_create_owner_post(self):
        response = self.client.post(
            path = reverse('petowner_view'),
            data = self.owner_post_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['writer'], self.user_data['username'])