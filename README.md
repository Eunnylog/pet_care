# pet_care
<big>User</big>

<dir>
setting<br/> 
아래 두 명령어로 makemigrations, migrate후에 db모델에 csv파일 넣어주기
python location_db.py<br/> 
python species_db.py<br/> 

기본 유저 만들기<br/> 
1-1.CreateSuperuser 먼저할것 혹은 <br/> 
1-1.log up first account에서 회원가입하기<br/> 
<br/> 
사용유저 만들기<br/> 
2.logup<br/> 
3.login<br/> 
4.change info<br/> 
5.del user<br/> 


<br/>
-review-
1. 리뷰 불러오기, 작성, 수정, 삭제 확인, 각 권한 확인.
<br/> 
-예약-
1. 글 작성 후 다른 아이디로 지원 가능한지 확인
2. 글 작성자라면 지원자 리스트 확인 후 지원자 선택 확인
<br/> 

마지막 작업시 해야되는것: users.model의 user.nickname에unique값 지정하기
작업 예정:owner post detail delete 진짜 삭제하지 않고 status값 바꾸기

</dir>


Frontend와 연결할 때, SerializerMethodField()로 serializer 커스텀하여 어떤 항목 가져올지


