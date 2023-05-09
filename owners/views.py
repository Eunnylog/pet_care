from django.shortcuts import render

'''
# owner_id가 맞나? user/writer랑 헷갈린다
class PetOwnerCommentView(APIView):
    def get(self, request, owner_id):
        # 댓글 요청 함수
        owner = PetOwner.objects.get(id=owner_id)
        comments = owner.owner_set.all()
        serializer = PetOwnerCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, owner_id):
        # 댓글 작성 함수
        serializer = PetOwnerCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, owner_id=owner_id)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PetOwnerCommentDetailView(APIView):
    def put(self, request, owner_id, comment_id):
        # 댓글 수정 함수
        comment = get_object_or_404(PetOwnerComment, id=comment_id)
        if request.user == comment.user:
            serializer = PetOwnerCommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, owner_id, comment_id):
        # 댓글 삭제 함수
        comment = get_object_or_404(PetOwnerComment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

# PetOwnerCommentSerializer 변형한 PetOwnerCommentCreateSerializer 만들어야할지 (js연결할때 확인을 해야하나?)
# Postman으로 테스트시 Header에 적어놔야함
'''
