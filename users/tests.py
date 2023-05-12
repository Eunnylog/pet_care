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


# 회원가입 테스트
class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse("sign_up")  # name을 이용해 회원가입 url 가져옴
        user_data = {   
            "username": "test",
            "email": "test@test.com",
            "password":"1234",
        }
        response = self.client.post(url, user_data)  # post에 url과 유저데이터 담아줌
        self.assertEqual(response.status_code, 201)


# 로그인 테스트
class LoginUserTest(APITestCase):
    def setUp(self):
        
        self.data = {"username": "test","email":"test@test.com", "password":"1234"}
        self.user = User.objects.create_user("test","test@test.com","1234")  # create_user는 models.py에 설정해준 메소드
    
    # 로그인 확인    
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code, 200)
    
    # 회원 정보 확인    
    def test_get_user_data(self):
        access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']
        response = self.client.get(
            path=reverse('sign'),
            HTTP_AUTHORIZATION = f"Bearer {access_token}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], self.data['username'])

