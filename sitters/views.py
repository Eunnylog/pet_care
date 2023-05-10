from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from sitters.models import PetSitter
from sitters.serializers import PetSitterSerializer


# 게시글 리스트
class PetSitterView(APIView):
    # 게시글 가져오기
    def get(self, request):
        sitters = PetSitter.objects.all()
        serializer = PetSitterSerializer(sitters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 작성하기
    def post(self, request):
        serializer = PetSitterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PetSitterDetailAPI(APIView):
    # 게시글 상세보기
    def get(self, request, pk):
        sitters = PetSitter.objects.all(pk)
        serializer = PetSitterSerializer(sitters)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 수정하기
    def put(self, request):
        serializer = PetSitterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # 게시글 삭제하기
    def delete(self, request, pk):
        sitters = self.get_object(pk)
        sitters.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)