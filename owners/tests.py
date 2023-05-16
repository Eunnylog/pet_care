from datetime import timedelta, datetime
from django.urls import reverse
from rest_framework.test import APITestCase
from owners.models import PetOwner, Location, Species, PetOwnerComment, SittersForOwnerPR
from users.models import User
import csv
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY # 이미지 업로드
from PIL import Image
import tempfile
from faker import Faker
from owners.serializers import PetOwnerSerializer, PetOwnerCommentSerializer, SittersForOwnerPRSerializer
import pytz
from django.utils import timezone

# 임시파일 생성
def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255,0,0,0)
    photo = Image.new('RGBA', size, color)
    return temp_file


# ========================================================  게시글 테스트 시작 ========================================================

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
                Location.objects.create(
                    city=row['city'],
                    state=row['state']
                )

        with open('./species_breeds.csv', newline='', encoding='UTF8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['writer'], self.user_data['username'])
    
    # 이미지 확인    
    def test_create_owner_post_with_photo(self):
        temp_file = tempfile.NamedTemporaryFile()  # 파이썬에서 제공하는 임시파일 만드는 방식
        temp_file.name = "image.png"
        image_file = get_temporary_image(temp_file)
        image_file.seek(0)
        owner_post_data = self.owner_post_data.copy()
        owner_post_data["photo"] = temp_file.read()  # 파일 데이터를 읽어와 owner_post_data 딕셔너리의 'photo' 필드에 저장
        
        # 전송
        response = self.client.post(
            path = reverse('petowner_view'),
            data=encode_multipart(data = self.owner_post_data, boundary=BOUNDARY),
            content_type = MULTIPART_CONTENT,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['writer'], self.user_data['username'])

        
# 오너 게시글 읽기 테스트        
class OwnerPostReadTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        cls.owner_posts = []
        for i in range(10):
            cls.user = User.objects.create_user(cls.faker.name(),cls.faker.email(), cls.faker.word())
            cls.owner_posts.append(
                PetOwner.objects.create(
                    title=cls.faker.sentence(), content=cls.faker.text(), writer=cls.user, species=cls.faker.word(), location=cls.faker.word(), # witer는 외래키이기 때문에 user
                    charge=cls.faker.pydecimal(left_digits=4, right_digits=2, positive=True),
                    reservation_start=cls.faker.date_time_between(start_date='now', end_date='+30d').replace(tzinfo=pytz.UTC), # 시간대 차이를 계산하기 위해 시간대 정보를 포함하는 aware datetime을 사용해야한다
                    reservation_end=cls.faker.date_time_between(start_date='+30d', end_date='+30d').replace(tzinfo=pytz.UTC),
                    ))
            
    def test_get_owner_post(self):
        for post in self.owner_posts:
            url = post.get_absolute_url()
            response = self.client.get(url)
            serializer = PetOwnerSerializer(post).data
            for k, v in serializer.items():
                self.assertEqual(response.data[k], v)
                
# 오너 게시글 수정 테스트
class OwnerPostPutTest(APITestCase):
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
        cls.faker = Faker()
        cls.owner_post = []
        cls.user = User.objects.create_user("test1", "test1@test.com", "1234")
        cls.owner_post.append(PetOwner.objects.create(
            title=cls.faker.sentence(), content=cls.faker.text(), writer=cls.user, species=cls.faker.word(), location=cls.faker.word(), # witer는 외래키이기 때문에 user
            charge=cls.faker.pydecimal(left_digits=4, right_digits=2, positive=True),
            reservation_start=cls.faker.date_time_between(start_date='now', end_date='+30d').replace(tzinfo=pytz.UTC), # 시간대 차이를 계산하기 위해 시간대 정보를 포함하는 aware datetime을 사용해야한다
            reservation_end=cls.faker.date_time_between(start_date='+30d', end_date='+30d').replace(tzinfo=pytz.UTC),
        ))

        
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']

    
    # 게시글 수정
    def test_put_owner_post(self):
        response = self.client.put(
            path=reverse("petowner_detail_View", kwargs={"owner_id": self.owner_post[0].id}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data={
                "title": "수정된 게시글",
                "content": "수정된 내용",
                "location": 2,
                "charge": "10000",
                "species": 2,
                "reservation_start": timezone.now()+timedelta(days=2),
                "reservation_end": timezone.now()+ timedelta(days=21)
            }
        )
        self.assertEqual(response.status_code, 200)

# 오너 게시글 삭제 테스트
class OwnerPostDeleteTest(APITestCase):
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
        cls.faker = Faker()
        cls.owner_post = []
        cls.user = User.objects.create_user("test1", "test1@test.com", "1234")
        cls.owner_post.append(PetOwner.objects.create(
            title=cls.faker.sentence(), content=cls.faker.text(), writer=cls.user, species=cls.faker.word(), location=cls.faker.word(), # witer는 외래키이기 때문에 user
            charge=cls.faker.pydecimal(left_digits=4, right_digits=2, positive=True),
            reservation_start=cls.faker.date_time_between(start_date='now', end_date='+30d').replace(tzinfo=pytz.UTC), # 시간대 차이를 계산하기 위해 시간대 정보를 포함하는 aware datetime을 사용해야한다
            reservation_end=cls.faker.date_time_between(start_date='+30d', end_date='+30d').replace(tzinfo=pytz.UTC),
        ))

        
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
    
    # 게시글 삭제
    def test_delete_owner_post(self):
        response = self.client.delete(
            path=reverse("petowner_detail_View", kwargs={"owner_id": self.owner_post[0].id}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 204)
# ======================================================== 게시글 테스트 끝 ========================================================   
    
# ======================================================== 댓글 테스트 시작 ========================================================      
# 댓글 작성 테스트
class OwnerCommentCreateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {"username": "test1","email":"test1@test.com", "password":"1234"}
        cls.owner_post_data = {
            "title": "테스트 게시글",
            "content": "테스트 합니다",
            "location": 1,
            "charge": "5000",
            "species": 1,
            "reservation_start": timezone.now()+timedelta(days=1),
            "reservation_end": timezone.now()+ timedelta(days=20)
        }
        cls.user = User.objects.create_user("test1","test1@test.com","1234")
        cls.owner_post = PetOwner.objects.create(   # 외래키 필드 값을 생성해주기 위해
            writer= cls.user,
            **cls.owner_post_data
        )
        cls.comment_data = {
            "writer" : cls.user.pk,
            "owner_post" : cls.owner_post.pk,
            "content" : "테스트 댓글입니다"
        }
        
        
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
    
        with open('./location_code.csv', newline='', encoding='UTF8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                Location.objects.create(
                    city=row['city'],
                    state=row['state']
                )

        with open('./species_breeds.csv', newline='', encoding='UTF8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                Species.objects.create(
                    species=row['species'],
                    breeds=row['breeds']
                )
    
        
    # 로그인 확인    
    def test_fail_if_not_logged_int(self):
        url = reverse('petowner_comment_view', kwargs={'owner_id': self.owner_post.pk})
        response = self.client.post(url, self.comment_data)
        self.assertEqual(response.status_code, 401)
            
    # 댓글 작성
    def test_create_comment(self):
        response = self.client.post(
        path = reverse('petowner_comment_view', kwargs={'owner_id': self.owner_post.pk}),
        data = self.comment_data,
        HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
    )
        self.assertEqual(response.status_code, 201)
        
        
        
# 댓글 읽기 테스트
class OwnerPostCommentReadTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        cls.owner_posts = []
        cls.post_comments = []
        for i in range(10):
            cls.user = User.objects.create_user(cls.faker.name(),cls.faker.email(), cls.faker.word())
            cls.owner_posts.append(
                PetOwner.objects.create(
                    title=cls.faker.sentence(), content=cls.faker.text(), writer=cls.user, species=cls.faker.word(), location=cls.faker.word(), # witer는 외래키이기 때문에 user
                    charge=cls.faker.pydecimal(left_digits=4, right_digits=2, positive=True),
                    reservation_start=cls.faker.date_time_between(start_date='now', end_date='+30d').replace(tzinfo=pytz.UTC), # 시간대 차이를 계산하기 위해 시간대 정보를 포함하는 aware datetime을 사용해야한다
                    reservation_end=cls.faker.date_time_between(start_date='+30d', end_date='+30d').replace(tzinfo=pytz.UTC),
                    ))
            cls.post_comments.append(
                PetOwnerComment.objects.create(
                    writer=cls.user, owner_post=cls.owner_posts[i], content=cls.faker.text()
                )
            )

    def test_get_owner_post_comments(self):
        for comment in self.post_comments:
            url = comment.get_absolute_url()
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            
            
# 댓글 수정 테스트
class OwnerPostCommentPutTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {"username": "test1","email":"test1@test.com", "password":"1234"}
        cls.owner_post_data = {
            "title": "테스트 게시글",
            "content": "테스트 합니다",
            "location": 1,
            "charge": "5000",
            "species": 1,
            "reservation_start": timezone.now()+timedelta(days=1),
            "reservation_end": timezone.now()+ timedelta(days=20)
        }
        cls.user = User.objects.create_user("test1","test1@test.com","1234")
        cls.owner_post = PetOwner.objects.create(   # 외래키 필드 값을 생성해주기 위해
            writer= cls.user,
            **cls.owner_post_data
        )
        cls.comment_data = {
            "writer" : cls.user,
            "owner_post" : cls.owner_post,
            "content" : "테스트 댓글입니다"
        }
        
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
        self.comment = PetOwnerComment.objects.create(**self.comment_data)
        
    # 댓글 수정
    def test_put_owner_post_comment(self):
        response = self.client.put(
            path=reverse("petowner_comment_detail_view", kwargs={"owner_id": self.owner_post.pk, 'comment_id': self.comment.pk}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data={
                'content':'댓글수정'
            }
        )
        self.assertEqual(response.status_code, 200)
        

# 댓글 삭제 테스트
class OwnerPostCommentDeleteTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {"username": "test1","email":"test1@test.com", "password":"1234"}
        cls.owner_post_data = {
            "title": "테스트 게시글",
            "content": "테스트 합니다",
            "location": 1,
            "charge": "5000",
            "species": 1,
            "reservation_start": timezone.now()+timedelta(days=1),
            "reservation_end": timezone.now()+ timedelta(days=20)
        }
        cls.user = User.objects.create_user("test1","test1@test.com","1234")
        cls.owner_post = PetOwner.objects.create(   # 외래키 필드 값을 생성해주기 위해
            writer= cls.user,
            **cls.owner_post_data
        )
        cls.comment_data = {
            "writer" : cls.user,
            "owner_post" : cls.owner_post,
            "content" : "테스트 댓글입니다"
        }
        
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
        self.comment = PetOwnerComment.objects.create(**self.comment_data)
        
    # 댓글 삭제
    def test_put_owner_post_comment(self):
        response = self.client.delete(
            path=reverse("petowner_comment_detail_view", kwargs={"owner_id": self.owner_post.pk, 'comment_id': self.comment.pk}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 204)
# ======================================================== 댓글 테스트 끝 ========================================================


# ======================================================== 예약하기 테스트 시작 ========================================================

# 시터가 오너의 게시글에 예약하기
# class SitterTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user_data = {"username": "test1","email":"test1@test.com", "password":"1234"} # 글작성자
#         cls.user2_data = {"username": "test2","email":"test2@test.com", "password":"1234"} # 글지원자
#         cls.owner_post_data = {
#             "title": "테스트 게시글",
#             "content": "테스트 합니다",
#             "location": 1,
#             "charge": "5000",
#             "species": 1,
#             "reservation_start": timezone.now()+timedelta(days=1),
#             "reservation_end": timezone.now()+ timedelta(days=20)
#         }
#         cls.user = User.objects.create_user("test1","test1@test.com","1234")
#         cls.user2 = User.objects.create_user("test2","test2@test.com","1234")
#         cls.owner_post = PetOwner.objects.create(   # 외래키 필드 값을 생성해주기 위해
#             writer= cls.user,
#             **cls.owner_post_data
#         )
#         cls.sitter_pr_data = {
#             "sitter": cls.user2,
#             "owner_post": cls.owner_post,
#             "is_selected": False
#         }

        
#     def setUp(self):
#         self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
#         self.access_token2 = self.client.post(reverse('token_obtain_pair'), self.user2_data).data['access']
#         self.sitter_pr = SittersForOwnerPR.objects.create(**self.sitter_pr_data)
    
    
#     # 로그인하지 않은 유저 접근 시 에러 작동 확인    
#     def test_fail_if_not_logged_int(self):
#         serializer = SittersForOwnerPRSerializer(self.sitter_pr)
#         url = reverse('sittersforownerpr_view', kwargs={"owner_id": self.owner_post.pk})
#         response = self.client.post(url, serializer.data)
#         self.assertEqual(response.status_code, 401)
    
#     # 예약하기 테스트
#     def test_pr_for_owner_post(self):
#         data = {'sitter':self.user2.id}
#         response = self.client.post(
#             path = reverse('sittersforownerpr_view',kwargs={"owner_id": self.owner_post.pk}),
#             data = data,
#             HTTP_AUTHORIZATION = f"Bearer {self.access_token2}"
#         )
#         self.assertEqual(response.status_code, 200)