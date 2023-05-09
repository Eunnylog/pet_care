from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from owners.models import PetOwner, PetOwnerComment
from owners.serializers import PetOwnerSerializer, PetOwnerCreateSerializer, PetOwnerCommentSerializer, PetOwnerCommentCreateSerializer


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


# 댓글 목록과 작성 
class PetOwnerCommentView(APIView):
    def get(self, request, owner_id):
        """댓글 요청 함수"""
        owner_post = PetOwner.objects.get(id=owner_id)
        comments = owner_post.petownercomment_set.all()
        serializer = PetOwnerCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, owner_id):
        """댓글 작성 함수"""
        serializer = PetOwnerCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user, owner_post_id=owner_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 댓글 수정, 삭제    
class PetOwnerCommentDetailView(APIView):
    def put(self, request, owner_id, comment_id):
        """댓글 수정 함수"""
        comment = get_object_or_404(PetOwnerComment, id=comment_id)
        if request.user == comment.writer:
            serializer = PetOwnerCommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, owner_id, comment_id):
        """댓글 삭제 함수"""
        comment = get_object_or_404(PetOwnerComment, id=comment_id)
        if request.user == comment.writer:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
