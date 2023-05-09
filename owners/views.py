from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# 게시글 목록과 작성
class PetOwnerView(APIView):
    def get(self, request):
        """게시글 목록 불러오기"""
        pass
    
    def post(self, request):
        """게시글 작성"""
        pass

    

# 게시글 상세페이지 수정, 삭제    
class PetOwnerDetailView(APIView):
    def get(self, request, pk):
        """게시글 상세보기"""
        pass
    
    def put(self, request, pk):
        """게시글 수정"""
        pass
    
    def delete(self, request, pk):
        """게시글 삭제"""
        pass