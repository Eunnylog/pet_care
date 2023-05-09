from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework import status
# from sitters.models import PetSitter, PetSitterComment
# from sitters.serializers import PetSitterSerializer, PetSitterCreateSerializer, PetSitterCommentSerializer, PetSitterCommentCreateSerializer




# Create your views here.
@api_view(['GET', 'POST'])
def sitter_view(request):
    return Response("확인")


'''
class PetSitterCommentView(APIView):
    def get(self, request, sitter_id):
        """댓글 요청 함수"""
        sitter_post = PetSitter.objects.get(id=sitter_id)
        comments = sitter_post.petsittercomment_set.all()
        serializer = PetSitterCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, sitter_id):
        """댓글 작성 함수"""
        serializer = PetSitterCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user, sitter_post_id=sitter_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PetSitterCommentDetailView(APIView):
    def put(self, request, sitter_id, comment_id):
        """댓글 수정 함수"""
        comment = get_object_or_404(PetSitterComment, id=comment_id)
        if request.user == comment.writer:
            serializer = PetSitterCommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, sitter_id, comment_id):
        """댓글 삭제 함수"""
        comment = get_object_or_404(PetSitterComment, id=comment_id)
        if request.user == comment.writer:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
'''