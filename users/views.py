from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import CustomTokenObtainPairSerializer,\
    UserSerializer,UserUpdateSerializer,UserUpdatePasswordSerializer,UserDelSerializer, \
    PetOwnerReviewCreateSerializer, PetSitterReviewCreateSerializer,PetOwnerReviewSerializer,PetSitterReviewSerializer,StarRatingSerializer,\
    MyPageSerializer
from users.models import CheckEmail, User, PetOwnerReview, PetSitterReview

from django.core.mail import EmailMessage

import base64
import random

def make64(sitename):
    sitename_bytes = sitename.encode('ascii')
    sitename_base64 = base64.b64encode(sitename_bytes)
    sitename_base64_str = sitename_base64.decode('ascii')
    return sitename_base64_str

#회원가입 이메일 확인
class SendEmail(APIView):
    def post(self,request):
        try:
            User.objects.get(email=email)
            return Response({"message":"아이디가 이미 존재합니다."},status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        subject='>_PetCare 인증메일'
        email=request.data.get("email")
        body=make64(email)
        email = EmailMessage(subject,body,to=[email],)
        email.send()
        return Response({"message":"이메일 확인하세요"},status=status.HTTP_200_OK)

#회원가입
class SignUp(APIView):
    def post(self,request):
        if make64(request.data.get("email"))!=request.data.get("check_email"):
            return Response({"message": f"이메일오류"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

#로그인
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#자신의 데이터
class UserView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    #자신의정보보기
    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #업데이트
    def put(self,request):
        check_password=request.data.get("check_password")
        password=request.data.get("password")
        user = request.user
        if user.check_password(check_password):
            serializer = UserUpdatePasswordSerializer(user,data=request.data)
        elif password =="" or password ==None:
            serializer = UserUpdateSerializer(user,data=request.data)
        else:
            return Response({"message":"패스워드가 다릅니다"},status=status.HTTP_401_UNAUTHORIZED)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    #삭제
    def delete(self,request):
        user = request.user
        datas=request.data
        datas["is_active"]=False
        serializer = UserDelSerializer(user,data=datas)
        print(serializer)
        if user.check_password(request.data.get("password")):
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"삭제완료!"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":f"패스워드가 다릅니다"}, status=status.HTTP_400_BAD_REQUEST)
    

#패스워드용 이메일확인
class SendPasswordEmail(APIView):
    def post(self,request):
        subject = '>_PetCare 8자리 인증번호'
        random_num = int(10**8*random.random())
        email = request.data.get("email")
        try:
            User.objects.get(email=email)
        except:
            return Response({"message":"아이디가 존재하지 않습니다"},status=status.HTTP_400_BAD_REQUEST)
        try:
            email_list=CheckEmail.objects.get(email=email)
        except:
            email_list=CheckEmail()
            email_list.email=email
        email_list.random_num=random_num
        email_list.save()
        random_num=str(random_num)
        #이메일 보내기
        send_email = EmailMessage(subject,random_num,to=[email],)
        send_email.send()
        return Response({"message":"인증번호를 확인하세요"},status=status.HTTP__200)

#비로그인 패스워드 바꾸기
class ChangePassword(APIView):
    def post(self,request):
        email=request.data.get("email")
        email_code=request.data.get("email_code")
        try:
            check_email=CheckEmail.objects.get(email=email)
            if check_email.random_num!=int(email_code):
                check_email.try_num+=1
                check_email.save()
                if check_email.try_num<=5:
                    return Response({"message":f"${check_email.try_num}/5 인증번호를 확인하세요"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message":f"${check_email.try_num}/5 24시간 횟수초과"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message":"이메일 인증이 안되었습니다"},status=status.HTTP_404_NOT_FOUND)
        user=get_object_or_404(User, email=email)
        serializer = UserUpdatePasswordSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
        check_email.delete()
        return Response({"message":"패스워드가 변경되었습니다."},status=status.HTTP_200_OK)

class PetOwnerReviewView(APIView):
    # 모든 후기 가져오기
    def get(self, request, user_id):
        owner = get_object_or_404(User,pk = user_id)
        ownerreviews = owner.ownerreviews.filter(show_status='1')
        serializer = PetOwnerReviewSerializer(ownerreviews, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 후기 작성하기
    def post(self, request, user_id):
        if request.user.is_authenticated:
            serializer = PetOwnerReviewCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(writer = request.user, owner_id = user_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': '로그인이 필요합니다.'}, status=status.HTTP_401_UNAUTHORIZED)


class PetOwnerReviewDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # 후기 상세보기
    def get(self, request, user_id, review_id):
        ownerreview = get_object_or_404(PetOwnerReview, pk=review_id, show_status='1')
        serializer = PetOwnerReviewSerializer(ownerreview)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 후기 수정하기
    def put(self, request, user_id, review_id):
        ownerreview = get_object_or_404(PetOwnerReview, pk=review_id, show_status='1')
        serializer = PetOwnerReviewCreateSerializer(ownerreview, data=request.data)
        if request.user == ownerreview.writer:
            if serializer.is_valid():
                serializer.save(writer = request.user, owner_id = user_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mesage': '권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)
    
    # 후기 삭제하기
    def delete(self, request, user_id, review_id):
        ownerreview = get_object_or_404(PetOwnerReview, pk=review_id, show_status='1')
        if request.user == ownerreview.writer:
            ownerreview.show_status='3'
            ownerreview.save()
            return Response({'mesage': '후기가 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'mesage': '권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)
    


class PetSitterReviewView(APIView):
    # 모든 후기 가져오기
    def get(self, request, user_id):
        sitter = get_object_or_404(User,pk = user_id)
        sitterreviews = sitter.sitterreviews.filter(show_status='1')
        serializer = PetSitterReviewSerializer(sitterreviews, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 후기 작성하기
    def post(self, request, user_id):
        if request.user.is_authenticated:
            serializer = PetSitterReviewCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(writer = request.user, sitter_id = user_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mesage': '권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)


class PetSitterReviewDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # 후기 상세보기
    def get(self, request, user_id, review_id):
        sitterreview = get_object_or_404(PetSitterReview, pk=review_id,show_status='1')
        serializer = PetSitterReviewSerializer(sitterreview)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 후기 수정하기
    def put(self, request, user_id, review_id):
        sitterreview = get_object_or_404(PetSitterReview, pk=review_id,show_status='1')
        serializer = PetSitterReviewCreateSerializer(sitterreview, data=request.data)
        if request.user == sitterreview.writer:
            if serializer.is_valid():
                serializer.save(writer = request.user, sitter_id = user_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mesage': '권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)
    
    # 후기 삭제하기
    def delete(self, request, user_id, review_id):
        sitterreview = get_object_or_404(PetSitterReview, pk=review_id,show_status='1')
        if request.user == sitterreview.writer:
            sitterreview.show_status='3'
            sitterreview.save()
            return Response({'mesage': '후기가 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'mesage': '권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)
    

# 유저의 후기 평점
class StarRatingView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk = user_id)
        serializer = StarRatingSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MyPageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, user_id):
        user = get_object_or_404(User, pk = user_id)
        if request.user == user:
            serializer = MyPageSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'mesage': '권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)