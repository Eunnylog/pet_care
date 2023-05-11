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

# class UserRegistrationTest(APITestCase):
#     def test_sign_up(self):
#         url = reverse("sign_up")
#         user_data = {
#         "username": "testuser",
#         "email": "test@testuser.com",
#         "password": "passtest"
#         }
#         response =self.client.post(url, user_data)
#         print(response.data)
#         self.assertEqual(response.status_code, 201)


#     def test_sign_in(self):
#         url = reverse("token_obtain_pair")
#         user_data = {
#         "username": "testuser",
#         "email": "test@testuser.com",
#         "password": "passtest"
#         }
#         response = self.client.post(url, user_data)
#         print(response.data)
#         self.assertEqual(response.status_code, 200)



class UserRegistrationTest(APITestCase):
    def setUp(self):
        self.data = {
            'username': 'testuser',
            'email': 'test@testuser.com',
            'password': 'passtest'
        }
        self.user = User.objects.create_user('testuser', 'test@testuser.com', 'passtest')

    def test_login(self):
        response = self.client.post(reverse("token_obtain_pair"), self.data)
        # print(response.data["access"])
        self.assertEqual(response.status_code, 200)

    #사용자 정보조회
    # access_token 받아오기=
    # self.client한테 post를 보냄
    # reverse("url의 name"): post 보낸 주소 <=여기까지 로그인 진행임
    # self.data<=로그인 진행하고 받아온 데이터
    # data['access'] 받아온 데이터의 access 데이터를 받아옴
    def test_get_user_data(self):
        access_token = self.client.post(reverse("token_obtain_pair"), self.data).data['access']
        #access토큰을 헤더에 실어서 get요청을 view url에 함
        response = self.client.get(
                path=reverse('sign_in'),
                HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['username'], self.data['username'])


#회원정보 수정


#회원 탈퇴
    # def tearDown(self,request):
    #     response = self.client.post(reverse("token_obtain_pair"), self.data)
    #     user = get_object_or_404(User,id=request.user.id)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(response.status_code, 204)

