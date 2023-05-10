from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from sitters.models import PetSitter
from sitters.serializers import PetSitterSerializer, PetSitterCreateSerializer


# 게시글 리스트
class PetSitterView(APIView):
    # 게시글 가져오기
    def get(self, request):
        sitters = PetSitter.objects.all()
        serializer = PetSitterSerializer(sitters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 작성하기
    def post(self, request):
        serializer = PetSitterCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PetSitterDetailAPI(APIView):
    # 게시글 상세보기
    def get(self, request, pk):
        sitters = PetSitter.objects.get(id=pk)
        serializer = PetSitterSerializer(sitters)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 수정하기
    def put(self, request, pk):
        sitters = PetSitter.objects.get(id=pk)
        if request.user == sitters.writer:  # 본인이 작성한 게시글이 맞다면
            serializer = PetSitterCreateSerializer(sitters, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:   # 본인의 게시글이 아니라면
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
    # 게시글 삭제하기
    def delete(self, request, pk):
        sitters = PetSitter.objects.get(id=pk)
        if request.user == sitters.writer:  # 본인이 작성한 게시글이 맞다면
            sitters.delete()
            return Response({'message':'게시글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        else:   # 본인의 게시글이 아니라면
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)