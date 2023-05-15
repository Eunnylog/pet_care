# Pet Care🐾

당신의 반려동물을 위한 최고의 돌봄 서비스, Pet Care입니다.
<br/>
Pet Care에서 간단한 요청글 게시하시고 가까운 펫 시터님에게 도움을 받아보세요.
<br/>
여러분의 소중한 반려동물을 자랑하며, 안심하고 돌봐줄 시터님을 직접 선택할 수 있습니다.
<br/>
Pet Care에서는 당신과 반려동물을 위한 편리하고 안전한 돌봄 서비스를 제공합니다.
<br/>
우리의 소중한 반려동물을 위한 서비스, Pet Care와 함께 하세요.
<br/>

![petcare](https://github.com/nueeng/pet_care/assets/127704498/a10cb810-539c-4ba9-bd78-5dddb800843b)

![Frontend Github](https://github.com/nueeng/pet_care_frontend)

## 📚 Stacks

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"><img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"><img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"><img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

## 🚩 Installation

`python manage.py makemigrations`, `python manage.py migrate`로 모델 생성 후
<br/>
`python location_db.py`, `python species_db.py`를 실행하여 검색어 지역과 종 DB를 csv로 넣어주세요.

## 💡 Features

1. 로그인, 회원 가입
    - 회원가입 기능
    - 로그인 기능
    - 로그아웃 기능
2. 게시글 CRUD 
    - 피드 페이지(펫시터 구해요)
        - 자기pr / 모집 별로 최신 게시글의 제목 or 썸네일 보기
        - 로그인 안 해도 다 볼 수 있게
    - 피드 페이지(펫시터 해드려요)
        - 자기pr / 모집 별로 최신 게시글의 제목 or 썸네일 보기
        - 로그인 안 해도 다 볼 수 있게
    - 게시글 작성 페이지(각 피드 페이지에서 가능)
        - 로그인한 사용자만 들어올수 있게!
    - 상세 게시글 페이지
        - 게시글의 세부내용 보기
        - 글 작성자만! 수정/삭제 가능하다
    - 댓글 작성
    - 후기 작성
    - 마이 페이지

## 📋 Procedure
<br/>

- Pet_owner(구인) 
1. 오너가 글을 작성한다. 
2. 시터들이 게시글을 확인 후 지원 신청한다(자기소개(실명), 성별, 나이, 어필사항) 
3. 오너는 시터가 작성한 신청서를 보고 마음에 드는 사람과 매칭 → 예약중 상태로 변경된다
4. 예약시작일이 되면 해당 글이 진행중으로 바뀐다. (매칭 취소 시 → 구인중 상태로 변경)
5. 예약 끝나는날이 되면 완료로 바뀐다.
6. 오너가 시터에 대한 리뷰를 작성한다(내용, 별점(5점만점)

<br/>

- Pet_sitter(구직)
1. 시터가 오너의 구인글을 본다
2. 시터가 지원서를 작성한다(자기소개(실명),성벌, 나이, 어필사항) 
3. 지원서와함께 신청한다 
4. 오너에게 선택 받으면 매칭 완료
5. 선택 받지 못할 시 매칭 실패
6. 시터가 오너에 대한 리뷰를 작성한다(내용, 별점(5점만점)

 ## Team
 
 - 박종민 : https://github.com/jmpop97
 - 공민영 : https://github.com/Kminy98
 - 김정은 : https://github.com/Eunnylog
 - 박혜린 : https://github.com/HyerinPark1998
 - 최준영 : https://github.com/nueeng  
