from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from owners.models import PetOwner, PetOwnerComment, SittersForOwnerPR, Location, Species
from owners.serializers import PetOwnerSerializer, PetOwnerCreateSerializer, PetOwnerCommentSerializer, PetOwnerCommentCreateSerializer, SittersForOwnerPRSerializer, LocationSerializer, SpeciesSerializer


# 게시글 목록과 작성
class PetOwnerView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 모든 게시글 불러오기
    def get(self, request):
        owner_posts = PetOwner.objects.filter(show_status='1').order_by('-created_at') # 모든 게시글
        serializer = PetOwnerSerializer(owner_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 작성하기
    def post(self, request):
        serializer = PetOwnerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

# 게시글 상세페이지 수정, 삭제    
class PetOwnerDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 게시글 상세보기
    def get(self, request, owner_id):
        owner_post = get_object_or_404(PetOwner, id = owner_id, show_status='1')
        serializer = PetOwnerSerializer(owner_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 수정하기
    def put(self, request, owner_id):
        owner_post = get_object_or_404(PetOwner, id = owner_id,show_status='1')
        # 본인이 작성한 게시글이 맞다면
        if request.user == owner_post.writer:
            serializer = PetOwnerCreateSerializer(owner_post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 본인의 게시글이 아니라면
        else:
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    # 게시글 삭제하기
    def delete(self, request, owner_id):
        owner_post = get_object_or_404(PetOwner, id=owner_id, show_status='1')
        # 본인이 작성한 게시글이 맞다면
        if request.user == owner_post.writer:
            owner_post.show_status = '3'
            owner_post.save() 
            return Response({'message':'게시글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        # 본인의 게시글이 아니라면
        else:
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


# 댓글 목록과 작성 
class PetOwnerCommentView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, owner_id):
        """댓글 요청 함수"""
        owner_post = get_object_or_404(PetOwner, id=owner_id)
        comments = owner_post.petownercomment_set.filter(show_status='1').order_by('-created_at')
        serializer = PetOwnerCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, owner_id):
        """댓글 작성 함수"""
        serializer = PetOwnerCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user, owner_post_id=owner_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 댓글 수정, 삭제
class PetOwnerCommentDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, owner_id, comment_id):
        """댓글 수정 함수"""
        comment = get_object_or_404(PetOwnerComment, id=comment_id, show_status='1')
        if request.user == comment.writer:
            serializer = PetOwnerCommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, owner_id, comment_id):
        """댓글 삭제 함수"""
        comment = get_object_or_404(PetOwnerComment, id=comment_id, show_status='1')
        if request.user == comment.writer:
            comment.show_status='3'
            comment.save()
            return Response({'message': '댓글이 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


# owner 에약하기
class SittersForOwnerPRView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, owner_id):
        post = get_object_or_404(PetOwner, id=owner_id)
        # 글 작성자와 로그인 된 유저가 같은 지 확인 후 리스트 불러오기
        if request.user == post.writer:
            reserved_list = SittersForOwnerPR.objects.filter(owner_post = owner_id)
            serializer = SittersForOwnerPRSerializer(reserved_list, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def post(self, request, owner_id):
        # 로그인 상태에서 예약 가능
        post = get_object_or_404(PetOwner, id=owner_id)
        # 글 작성자는 예약 불가
        if post.writer == request.user:
            return Response("글 작성자는 지원이 불가능합니다.", status=status.HTTP_200_OK)
        else:
            # 지원 여부 확인 후 진행
            if post.sittersforownerpr_set.filter(sitter = request.user):
                return Response("이미 지원하신 게시글입니다.", status=status.HTTP_200_OK)
            else:
                reserved = SittersForOwnerPR(owner_post = post, sitter = request.user)
                reserved.save()
                return Response("지원이 완료 되었습니다.", status=status.HTTP_200_OK)

# 시터 선택, 취소
class SitterIsSelectedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # 시터 선택하기
    def put(self, request, owner_id, user_id):
        post = get_object_or_404(PetOwner, id=owner_id)
        # 시터 선택 시 글 작성자와 로그인 된 유저가 동일한지 확인
        if request.user == post.writer:
            # 이미 시터 매치가 되었는 지 확인
            checking = SittersForOwnerPR.objects.filter(owner_post = owner_id, is_selected = True)
            if checking:
                # 이미 매치가 되어 있는 사람이라면 취소하기
                selected_sitter = get_object_or_404(SittersForOwnerPR, owner_post = owner_id, is_selected = True)
                if selected_sitter.sitter_id == user_id:
                    selected_sitter.is_selected = False
                    selected_sitter.save()
                    return Response("매치가 취소되었습니다.", status=status.HTTP_200_OK)
                else:
                    # 이미 시터가 있는 상태에서 다른 사람을 선택하려고 할 때
                    return Response("이미 매치가 된 게시글입니다.", status=status.HTTP_200_OK)
            else:
                # 시터 매치하기
                selected = get_object_or_404(SittersForOwnerPR, owner_post = owner_id, sitter = user_id)
                selected.is_selected = True
                selected.save()
                return Response("sitter와 매치되었습니다.", status=status.HTTP_200_OK)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)


# 지역정보 View
class LocationList(generics.ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = Location.objects.all()

        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city__icontains=city) # contains = 포함하는 문자열찾기 i가 붙으면 대소문자 구분 X

        state = self.request.query_params.get('state', None)
        if state is not None:
            queryset = queryset.filter(state__icontains=state)

        return queryset
    
    
# 품종정보 View
class SpeciesList(generics.ListAPIView):
    serializer_class = SpeciesSerializer

    def get_queryset(self):
        queryset = Species.objects.all()

        species = self.request.query_params.get('species', None)
        if species is not None:
            queryset = queryset.filter(species__icontains=species)

        breeds = self.request.query_params.get('breeds', None)
        if breeds is not None:
            queryset = queryset.filter(breeds__icontains=breeds)

        return queryset
    