![header](https://capsule-render.vercel.app/api?type=waving&color=0064ff&height=100&section=header&fontSize=90)


<br><br>

---
# Target site

* ## 사이트 소개  
    [Site Link](https://ridibooks.com/ebook/only)
    
* ## 사이트 선정 이유
    * 깔끔한 UI
    * 이커머스의 기본 기능인 로그인, 회원가입, 상품 조회, 옵션 선택, 장바구니, 주문 기능을 모두 담고 있음

<br><br>

---
# 초기기획 & ERD

## ERD

## User flow

## 초기기획 및 구현 목표
* 짧은 기간동안 기능구현에 집중해야하므로 사이트의 디자인과 기획만 클론
* 개발은 초기세팅부터 전부 직접 구현
* 사이트 카테고리 중 '도서'탭만 구현
* 필수 구현 사항을 회원가입, 로그인,상품리스트, 상품 조회, 장바구니, 주문기능으로 설정 

<br><br>

---
# 개발기간 및 팀원

* ## 개발기간  
    2022.03.14 ~ 2022.03.24  
    Sprint planning - 1 week

* ## 개발인원 및 파트

    * Front-end  
        김준영 - 초기세팅, 소셜로그인
        이희수 - 상품 리스트를 포함한 메인페이지, 네비게이션 바, footer
        한영현 - 리뷰와 책 시리즈 리스트를 포함한 상품 상세페이지, 장바구니 
        
    * Back-end   
        김광일 - 소셜로그인, 장바구니 API, 주문API
        임정찬 - 상품 리스트 API, 상품 상세 API
        김지성 - 리뷰 API, 좋아요API, AWS 배포(EC2, RDS)
<br><br>

---
# 적용 기술 및 구현 기능

* ## 기술 스택
    * ### Front-end  
        <a href="#"><img src="https://img.shields.io/badge/HTML-DD4B25?style=plastic&logo=html&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/SASS-254BDD?style=plastic&logo=sass&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/javascript-EFD81D?style=plastic&logo=javascript&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/React-68D5F3?style=plastic&logo=react&logoColor=white"/></a>
    * ### Back-end  
        <a href="#"><img src="https://img.shields.io/badge/python-3873A9?style=plastic&logo=python&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Django-0B4B33?style=plastic&logo=django&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/MySQL-005E85?style=plastic&logo=mysql&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS-FF9701?style=plastic&logo=aws&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/bcrypt-525252?style=plastic&logo=bcrypt&logoColor=white"/></a>
     <a href="#"><img src="https://img.shields.io/badge/postman-F76934?style=plastic&logo=postman&logoColor=white"/></a>
    * ### Common  
        <a href="#"><img src="https://img.shields.io/badge/git-E84E32?style=plastic&logo=git&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/RESTful API-415296?style=plastic&logoColor=white"/></a>
    * ### Communication  
        <a href="#"><img src="https://img.shields.io/badge/github-1B1E23?style=plastic&logo=github&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Slack-D91D57?style=plastic&logo=slack&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Trello-2580F7?style=plastic&logo=trello&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Notion-F7F7F7?style=plastic&logo=notion&logoColor=black"/></a>
* ## 구현기능
    * 소셜 로그인
        - 카카오 로그인 API를 사용한 소셜로그인 구현 
    * 상품 리스트 페이지
        - 메인페이지에 상품 리스트 포함
        - q객체를 이용한 카테고리별 필터링
        - annotate를 이용한 평균 별점 오름차순 정렬
        - order_by('?')를 이용해서 페이지 새로고침 시 무작위 작품 노출
    * 상품 상세 페이지
        - limit, offset 방식을 이용한 pagenation 구현
    * 리뷰
        - 각각의 유저가 1개의 상품에 1개의 리뷰만 달 수 있도록 구현
        - limit,offset을 이용한 pagenation 구현
    * 좋아요
        - 하나의 리뷰가 몇개의 좋아요를 받았는지 엔드포인트로 전달
    * 장바구니
        - select_related를 통한 ORM 최적화
        - 모듈화를 이용해 분기처리시 코드의 가독성 향상
    * 주문
        - 모듈화를 이용해 분기처리시 코드의 가독성 향상
<br><br>

---
# API 기능정의서
추후 

<br><br>

---
# 시연 영상
추후 추가 예정

<br><br>
---
# Reference
* 이 프로젝트는 [설로인](https://www.sirloin.co.kr/) 사이트를 참조하여 학습목적으로 만들었습니다.
* 실무수준의 프로젝트이지만 학습용으로 만들었기 떄문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
* 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다
* 이 프로젝트에서 사용하고 있는 로고와 배너는 해당 프로젝트 팀원 소유이므로 해당 프로젝트 외부인이 사용할 수 없습니다

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0064ff&height=100&section=footer)
