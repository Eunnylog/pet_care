from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from owners.models import PetOwner
from owners.serializers import PetOwnerSerializer, PetOwnerCreateSerializer

# 게시글 목록과 작성
class PetOwnerView(APIView):
    def get(self, request):
        """게시글 목록 불러오기"""
        owner_list = PetOwner.objects.all() # 모든 게시글
        serializer = PetOwnerSerializer(owner_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PetOwnerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

# 게시글 상세페이지 수정, 삭제    
class PetOwnerDetailView(APIView):
    def get(self, request, owner_id):
        """게시글 상세보기"""
        owner_post = PetOwner.objects.get(id=owner_id)
        serializer = PetOwnerSerializer(owner_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, owner_id):
        """게시글 수정"""
        pass
    
    def delete(self, request, owner_id):
        """게시글 삭제"""
        pass