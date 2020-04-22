DB 기본 용어

- DB : 여러사람이 공유 & 사용할 목적으로 체계화해 통합, 관리하는 데이터의 집합
- DBMS : DB Management System
- RDBMS : 관계형(table(row, col)) 모델기반
- 스키마 : 자료의 구조와 제약조건 명세
- 테이블 : 관계(row, col)
- col, 속성 : 고유한 데이터 형식
- row, 레코드 : table data
- pk : id, 레코드 고유 식별값

데이터 관계

1. 관계없음
2. 1:1 : 사람(주민등록번호)
3. 1:N : 학급:학생, 게시글:댓글
4. M:N : 게시글:좋아요 (이유는 나중에!!! ㄷㄷㄷㅈ)

SQL

> Structured Query Language)
>
> RDBMS위한 프로그래밍 언어

- DDL (Deginition) : 정의
- DML (Manupulation) : 조작
- DCL (Control) : 제어

Hello, world!

```sqlite
sqlite3 <filename> # SQLite3 생성/접근
# .으로 시작하는 문법 : SQLite 조작 위한 문법 
.tables # 테이블 목록 조회
.schema <talbe> # 특정 테이블 스키마 조회

# ;으로 끝나는 문법 : sql 문법, 키워드 구분위해 대문자로 작성(소문자 가능)
SELECT * FROM <table>; # 테이블 반환
CREATE TABLE <table>(
	<col1> datatype [constraints],
   	<col2> datatype [constraints],
);
# 닫기 : ctrl+d or .exit
```

sql 문법(SQLite)

- 캡쳐
- 예시 - 캡쳐

테이블

- **삭제** : **DROP TABLE** table_name;

레코드

- **추가 C** :**INSERT INTO** table_name (col_name, ...) **VALUES** (<val1>, ...);
  - **INSERT INTO** table_name **VALUES** (col_val, ...);
    - 모든 열에 데이터를 넣을 때에는 col_name 명시 불필요
- **조회 R** : **SELECT** col_name **FROM** table_name **WHERE** conditions;
- **수정 U** : **UPDATE** table_name **SET** <col1=val1,...> **WHERE** conditions;
- **삭제 D** : **DELETE** FROM table_name **WHERE** conditions;
- **SELECT**<col>
  - **DISTINCT**<col> : 중복 없이
  - **COUNT**<col> : 
    - **AVG**, **SUM**, **MAX**, **MIN**
- **FROM** <table> 
- **WHERE** <condition1> **AND**<cond2>
  - **LIKE** <col> '구문'
- **GROUP BY** <col>
- **ORDER BY** <col> [**ASC**/**DESC**]
  - ASC(default) : 오름차순
  - DESC : 내림차순
  - 다수 : 왼족부터
- **LIMIT** <integer>
  - **LIMIT** <integer> **OFFSET** <integer>
- ;



와일드 카드

- `%` : 문자열이 있을 수도 있다.
- `_` : 반드시 한 개의 문자가 있다.

<col>**_without_schema**

- 숫자 > 텍스트처럼 정렬 가능

에러 출력

- `NOT NULL constarint filed : <col>` : 항목 추가시 필수 항목 누락
- `UNIQUE constraint failed: <table>.<col>` : 유일값 오류

비주얼라이저 검색해보기

- .header on
- .mode column

like와 regular expression



0420 연습

```sql
sqlite3 db명
CREATE TABLE 테이블명(
	칼럼명 칼럼속성,
);
INSERT INTO 테이블명 (속성1, 속성2) VALUES (값1, 값2);
SELECT * FROM 테이블명
SELECT 칼럼명 FROM 테이블명
SELECT 칼럼명1, 칼럼명2 FROM 테이블명 WHERE 조건1
SELECT 칼럼명1, 칼럼명2 FROM 테이블명 WHERE 조건1 and 조건2
SELECT * FROM 테이블명 WHERE 칼럼명 like 'regular expression'
_한글자, %여러글자
UPDATE 테이블명 SET 칼럼명=수정사항 WHERE 수정할레코드조건;
DELETE FROM 테이블명 WHERE 삭제할레코드조건;
DROP TABLE 테이블명;

```



`SELECT id, flight_num FROM flights WHERE price<600;`

`SELECT departure FROM flights WHERE arrival='Incheon' and price>=500;`

`SELECT id, flight_num FROM flights WHERE flight_num like '__0%2' and waypoint='Beijing';`

- regular expression
- __0%2

```sql
UPDATE 테이블명 SET col수정사항 WHERE 수정할레코드;
```

- `UPDATE flights SET waypoint='Tokyo' WHERE flight_num='SQ0972'`

- 
- `DELETE FROM flights WHERE flight_num='RT9122'`

`DROP TABLE flights;`

- 이후 에러 `no such table: flights`



오후수업

django > model > makemigations > migrate

sql > table > create table

- .tables
- .schema 앱_모델
- .read 파일명 : 파일에 적힌 명령어 실행하기



0421수업

FK : 외부키 (PK)

유저(1) : 게시글(N)

```python
reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#on_delete : 항공사가 지워질때 항공편 모두 지우느냐
```

```python
r1.article_set.all()
Article.objects.get(pk=1).reporter.article_set.all()
```

```python
"reporter_id" INTEGER NOT NULL REFERENCES "articles_reporter" ("id")
```



## 1:N

- 1 has many N
  - `1`.`N`_set.all()

- N must belong to 1
  - `2`.`1`
  - `2`.`1`_id  

- python manage.py shell_plus --print-sql

- 야 장고, 디비쉘 열어봐
  - python manage.py dbshell

- 데이터 seeding (header 옵션 지정해야)

```sql
.mode csv
.import 파일명 테이블명
```

```sql
 .headers on
```

exercise

```python
# 1. SELECT 8 FROM users_user;
User.objects.all()
# 2. SELECT age FROM users_user WHERE id = 19;
User.objects.get(id=19).age
# 3. SELECT age FROM users_user
User.objects.all().values('age')
# 4. SELECT id, balance FROM users_user WHERE age <= 40;
User.objects.filter(age__lte=40).values('id', 'balance')
# 5. SELECT first_name FROM users_user WHERE last_name ="김" AND balance >= 500;
User.objects.filter(last_name = '김', balance__gte=500).values('first_name')
# 6. SELECT balance FROM users_user WHERE first_name LIKE = '%수' AND country = '경기도';
for u in User.objects.filter(first_name__contains = '%수', country = '경기도'):
    print(u.balance)
# 7
User.objects.filter(Q(balance__bte=2000) | Q(age__lte=40)).count()
# 8
User.objects.filter(phone__starstwith='010').count()
# 9
for u in User.objects.filter(first_name='옥자', last_name='김'):
    u.country = '도'
    u.save()
User.objects.filter(first_name='옥자', last_name='김').update(country='경기도') 
# 10
for u in User.objects.filter(first_name='진호', last_name='백'):
    u.delete()
User.objects.filter(first_name='진호', last_name='백').delete()
# 9, 10 {update/delete}는 <queryset>과 <개별객체> 모두 적용 가능
# 11
User.objects.order_by('-balance')[:4].values('first_name','last_name','balance')
User.objects.order_by('-balance').values('first_name','last_name','balance')[:4]
# SQL 인덱스 누락에 따른 과부하 > queue > aws sqs
# 12
User.objects.filter(phone_contains='123', age__lt = 30)
# 13
User.objects.filter(phone_startswidth='010').values('country').distinct()
# 14
User.objects.all().aggregate(Avg('age'))
# 15
User.objects.filter(last_name="박").aggregate(Avg('balance'))
# 16
User.objects.filter(country="경상북도").aggregate(Max('balance'))
# 17
User.objects.filter(country="제주특별자치도").order_by('-balance').values('first_name').first()
User.objects.filter(country="제주특별자치도").order_by('-balance').first().first_name
```

- on_delete : 참조 대상이 삭제되는 경우
  - 여러 경우
    - 글O > 탈퇴 거부
    - 글X > 탈퇴 허용
    - 글O > 탈퇴 > 글 삭제
    - 글O > 탈퇴 > 글id를 ghost의 id로 변경
  - CASCADE : 해당 객체(글)가 삭제 되었을 때, 참조하는 객체(댓글)도 모두 삭제
  - PROTECT : 참조하는 객체(댓글)가 존재하면 객체(글) 삭제 금지
  - SET_NULL : NULL값으로 치환, NOT NULL 옵션이 있는 경우는 활용 불가
  - SET_DEFAULT : 디폴트 값을 참조하게끔 한다.

# 장고 폼

```python
from django.db import models
from django.conf import settings
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 어느 app의 model인지의 정보
```

- 글쓰기창 > user를 선택하게 되어있음 > 무엇을 수정할것인가? > form

```python
# 필요한 field만 선택한다
field = ['title', 'content']
```

- IntegrityError 무결성 에러

  - NOT NULL constratint failed: articles_article.user_id

- create 로직에서 id를 넘길 수 있도록 수정 필요

  - modelform 응용

    ```python
    article = form.save(commit=False)
    article.user = request.user
    article.save()
    ```

- article.user : User **인스턴스** > 출력시 String
- article.user.username : **String**

다른 아이디에서 수정 삭제 버튼 안 보이도록 바꾸기

- **{% if article.user == request.user%}**
- 게시글 유저 == 로그인 유저

디테일 페이지에 댓글 기능 추가

- action 기능 필요 > 디테일은 보여주는 창이기 때문.
  - path(`<int:pk>/create/`, views.comment_craete, name='comments_create')
  - {% url 'articles:comments_create' article.pk %}

views.py

```python
def comments_create(request, pk):
    form = ComeentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
        return render('articles:detail', article.pk)
```

댓글목록 detail.py

```python
{% for comment in article.comment_set.all %}
	{{comment.user.username}}{{comment.content}}
{% endfor %}
```

# 0422 수업

```python
django-admin startproject 프로젝트이름
ALLOWED_HOSTS = ['*']
TZ, LCC 변경
python manage.py startapp 앱이름
INSTALLED_APPS 앱등록
앱의 urls.py 생성 (메인 urls.py와 연결)
# 모델 정의
class 모델명(models.Model):
    변수 = models.XxxField(...)
    변수 = ForiegnKey(...) #변수_id
# 모델폼 정의 : 1. 모델의 정의된 필드 사용 2. valid 검증 > HTML 반환
class 모델명Form(forms.ModelForm):
    class Meta:
        model = 모델명
        field = ['항목']
# 코드 작성 흐름 U V T
# U
path('경로', views.이름, name='url이름')
# V 함수 (인자 -> 반환)
def 이름 (request, pk): #http request, variable
    Model > Query Method
    Template > context
    # HTTP response obj
    return render (request, 'html', context)
	return redirect ('앱이름:url이름')
# T : DTL을 통해 HTML 작성
# 인자 : context, (context-processors >)request, request.user
{% extends 'base.html' %} # 탐색순서 1.DIR 2.APP_DIRS (Installed_Apps)

# Static : App별 static
{% load static %}
# staticfiles_dir..
```

django 기본

- 클래스 / 상속
- Name(import, 변수)

- 함수와 클래스
  - 함수 : 로직 재사용
  - 클래스 : 패턴 { 동작(메서드), 상태(변수) } 
    - OOP 객체지향프로그래밍 == S + V

# AUTH

user 모델 가져와 사용한다.

회원가입 User UserCreationForm	ModelForm

로그인 	X	  { AuthenticationForm	Form } >  request가 중요 > 첫번째 인자

# ERD

> Entity - Relationship Diagram

관계차수 / 카디널리티 (Database Cardinality 논리적 관계)

- 1:1 : (직선)
- 1:N  : (까마귀발) 
- Madatory (직선) : 1부터 시작 가능
- Optional (원) : 0부터 시작 가능
- M:N 