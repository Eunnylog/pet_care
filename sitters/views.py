
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from sitters.models import PetSitter
from sitters.serializers import PetSitterSerializer


# @api_view(['GET', 'POST'])
# #게시글 리스트
# def PetSitterView(request):
#         sitters = PetSitter.objects.all()
#         sitter = sitters[0]
#         sitter_data = {
#             "writer":sitter.writer,
#             "title":sitter.title,
#             "content":sitter.content,
#             "charge":sitter.charge,
#             "species":sitter.species,
#         }
#         return Response(sitter_data)

# Create your views here.
# @api_view(['GET', 'POST'])
# #게시글 리스트
# def PetSitterView(request):
#     if request.method == 'GET':
#         sitters = PetSitter.objects.all()
#         serializer = PetSitterSerializer(sitters, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PetSitterSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # 게시글 작성
# # @login_required(login_url='login')
# def create_post(request):
#     if not request.user.is_authenticated:
#         return redirect("/main")
#     if request.method == 'POST':
#         user_id = request.user.id  # 로그인한 사용자의 id 값을 가져옴
#         title = request.POST.get('title')
#         main_content = request.POST.get('main_content')
#         category = request.POST.get('category')

#         posting = Posting.objects.create(username_id=user_id,  # username 필드에 로그인한 사용자의 id 값을 입력
#                                          title=title,
#                                          main_content=main_content,
#                                          category=category)

#         return redirect('posting_detail', posting_id=posting.posting_id)
#     else:
#         return render(request, 'posting/posting_admin.html')


# # 게시글 수정
# @login_required(login_url='login')

# def update_post(request, posting_id):
#     posting = get_object_or_404(Posting, posting_id=posting_id, username=request.user)

#     if request.method == 'POST':
#         title = request.POST.get('title')
#         main_content = request.POST.get('main_content')
#         category = request.POST.get('category')

#         posting.title = title
#         posting.main_content = main_content
#         posting.category = category
#         posting.save()

#         return redirect(reverse('posting_detail', kwargs={'posting_id': posting_id}))
#     else:
#         context = {'posting': posting}
#         return render(request, 'posting/posting_admin.html', context)


# # 게시글 삭제
# @login_required(login_url='login')
# def delete_post(request, pk):
#     posting = get_object_or_404(Posting, posting_id=pk, username=request.user)
#     if request.method == 'POST':
#         posting.delete()
#         return redirect('posting_list')
#     else:
#         context = {'posting': posting}
#         return render(request, 'posting/posting_confirm_delete.html', context)


# def posting_admin(request):
#     return render(request, 'posting/posting_admin.html')