from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response

from users.serializers import UserSerializer,UserUpdateSerializer,UserUpdatePasswordSerializer, PetOwnerReviewCreateSerializer, PetSitterReviewCreateSerializer,PetOwnerReviewSerializer,PetSitterReviewSerializer,StarRatingSerializer,MyPageSerializer
from users.models import PetOwnerReview, PetSitterReview, User



#회원가입
class SignUp(APIView):
    def post(self,request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
#자신의 데이터
class UserView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    #자신의정보보기
    def get(self,request):
        user = get_object_or_404(User,id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #업데이트
    def put(self,request):
        check_password=request.data.get("check_password")
        password=request.data.get("password")
        print(password)
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
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

    #삭제
    def delete(self,request):
        user = get_object_or_404(User,id=request.user.id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

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