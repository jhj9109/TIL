# SQL과 django ORM

## 참고문서

[Making queries | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/queries/#making-queries)

[QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#queryset-api-reference)

[Aggregation | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation)

## **기본 준비 사항**

> Gitlab에서 프로젝트를 다운받으면 아래의 내용이 이미 반영되어 있습니다.

- django app
    - `django_extensions` 설치
    - `users` app 생성
    - csv 파일에 맞춰 `models.py` 작성 및 migrate

            $ python manage.py sqlmigrate users 0001

- `db.sqlite3` 활용 및 데이터 반영
    - `sqlite3` 실행

            $ ls
            db.sqlite3 manage.py ...
            $ sqlite3 db.sqlite3

    - csv 파일 data 로드

            sqlite > .tables
            auth_group                  django_admin_log
            auth_group_permissions      django_content_type
            auth_permission             django_migrations
            auth_user                   django_session
            auth_user_groups            auth_user_user_permissions
            users_user
            sqlite > .mode csv
            sqlite > .import users.csv users_user
            sqlite > SELECT COUNT(*) FROM users_user;
            1000

- 확인
    - sqlite3에서 스키마 확인

            sqlite > .schema users_user

## **문제**

> 아래의 문제들을 sql문과 대응되는 orm을 작성 하세요.

### Table 생성

- django

    ```python
    # django
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    # python manage.py makemigrations
    # python manage.py migrate
    ```

- SQL
    - sql.sqlite3에 동일하게 테이블 생성

        ```sql
        --sql
        ```

### 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   users = User.objects.all()
   # QuerySet
   print(users.query)
   ```

      ```sql
   -- sql
   SELECT * FROM users_user;
   -- table
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(
   	first_name="이름",
   	last_name="성",
       age=100,
       country="서울",
       phone="010-0000-0000",
       balance=10000
   )
   # <User: User object (101번째)>
   ```

   ```sql
   -- sql
   INSERT INTO users_user
   ('first_name', 'last_name', 'age', 'country', 'phone', 'balance')
   VALUES('이름', '성', 100, '서울', '010-0000-0000', 10000)
   -- NOT NULL contraint failed: 테이블명.칼럼명
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

     ```python
     # orm
     NOT NULL contraint failed: 모델명.필드명
     ```

     ```sql
     -- sql
     NOT NULL contraint failed: 테이블명.칼럼명
     ```

     

3. 해당 user 레코드 조회

   ```python
   # orm
   모델명.objects.get(칼럼명=값)
   # <모델명: 모델명 object (n번째)>
   ```

   - `get`은 쿼리 결과가 반드시 하나여야 한다. 이외에는 모두 오류를 반환한다.

     ```python
     # 여러개 존재시
     MultipleObjectsReturned
     # 0개 존재시
     DoesNotExist
     ```

     

      ```sql
   -- sql
   SELECT * FROM 테이블명 WHERE 칼럼명=값;
      ```

4. 해당 user 레코드 수정

   ```python
   # orm
   인스턴스 = 모델명.objects.get(칼럼명=값)
   인스턴스.칼럼명 = 값
   인스턴스.save()
   ```

      ```sql
   -- sql
   UPDATE 테이블명 SET 칼럼명=값 WHERE 레코드조건;
      ```

5. 해당 user 레코드 삭제

   ```python
   # orm
   모델명.objects.get(칼럼명=값).delete()
   ```
```
   
      ```sql
   -- sql
   DELETE FROM 테이블명 WHERE 레코드조건;
```

### 조건에 따른 쿼리문

1. 전체 인원 수

   ```python
   # orm
   모델명.objects.all().count()
   모델명.objects.count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM 테이블명;
      ```

2. 나이가 30인 사람의 이름

   ```python
   # orm
   모델명.objects.filter(조건).values('칼럼명')
   #=> queryset
   모델명.objects.filter(조건).values('칼럼명').query
   #=> SELECT "테이블명"."칼럼명 " FROM "테이블명" WHERE "테이블명".조건
   모델명.objects.filter(조건).values('칼럼명')[인덱스]
   #=> dict
   ```

      ```sql
   -- sql
   SELECT 칼럼명 FROM 테이블명 WHERE age = 30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   ```python
   # orm
   모델명.objects.filter(조건)
   # __gte >=, __gt >, __lte <=, __tl <
   ```

   - 대소관계

     > ex) 칼럼명__gte=값
     >
     > `__gte`  >=
     >
     > `__gt` >
     >
     > `__lte` <=
     >
     > `__tl` <

      ```sql
   -- sql
   SELECT COUNT(*) FROM 테이블명 WHERE 조건1;
      ```

4. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm 1
   모델명.objects.filter(조건1).filter(조건2).count( )
   # orm 2
   모델명.objects.filter(조건1, 조건2).count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM 테이블명 WHERE 조건1 and 조건2 ;
      ```

5. 지역번호가 02인 사람의 인원 수

   > https://docs.djangoproject.com/en/2.2/topics/db/queries/#escaping-percent-signs-and-underscores-in-like-statements
   >
   > ```
   > iexact, contains, icontains, startswith, istartswith, endswith, iendswith
   > ```

   ```python
   # orm
   모델명.objects.filter(칼럼명__명령어='패턴').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM 테이블명 WHERE 칼럼명 LIKE '패턴';
      ```

   - `_` : 한 글자
   - `%` : 여러 글자

6. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   모델명.objects.filter(조건1).filter(조건2).value(칼럼명)
   ```
   
   ```sql
   -- sql
   SELECT 칼럼명 FROM 테이블명
   WHERE 조건1 and 조건2
   ```
   
   

### 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람 10명 (내림차순)

   ```python
   # orm
   모델명.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM 테이블명
   ORDER BY 칼럼명
   DESC -- 오름차순
   LIMIT 숫자;
      ```

2. 잔액이 적은 사람 10명 (오른차순)

   ```python
   # orm
   모델명.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM 테이블명
   ORDER BY 칼럼명
   ASC
   LIMIT 숫자;
      ```

3. 성, 이름 내림차순 순으로 5번째 있는 사람

      ```python
   # orm
   모델명.objects.order_by('-칼럼명1', '-칼럼명2')[4]
   ```
   
   ```sql
   -- sql
   SELECT * FROM 테이블명
   ORDER BY 칼럼명1 DESC, 칼럼명2 DESC
   LIMIT 1 OFFSET 4;
   ```
   
   



### 표현식

> 표현식을 위해서는 [aggregate]([https://docs.djangoproject.com/en/2.2/topics/db/aggregation/](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/)) 를 알아야한다.

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   모델명.objects.aggregate(AVG('칼럼명'))
   ```

      ```sql
   -- sql
   SELECT AVG(칼럼명) FROM 테이블명;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   모델명.objects.filter(조건).aggregate(AVG('칼럼명'))
   ```

      ```sql
   -- sql
   SELECT AVG(칼럼명) FROM 테이블명 WHERE 조건;
      ```

3. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   from django.db.models import Max
   모델명.objects.aggregate(Max('칼럼명'))
   ```

      ```sql
   -- sql
   SELECT MAX(칼럼명) FROM 테이블명
      ```

4. 계좌 잔액 총액

      ```python
   # orm
   from django.db.models import SUM
모델명.objects.aggregate(Sum('칼럼명'))
   ```
   
      ```sql
   -- sql
   SELECT SUM(칼럼명) FROM 테이블명
      ```



### Group by

> annotate(뜻: 주석을 달다)는 개별 item에 추가 필드를 구성한다.
> 추후 1:N 관계에서 활용된다.

1. 지역별 인원 수

   ```python
   # orm
   모델.objects.values('칼럼명')
   from django.db.models import Count
   모델.objects.values('칼럼명').annotate(Count('칼럼명'))
   ```
   
   ```sql
   -- sql
   SELECT 칼럼명, COUNT(칼럼명) FROM 테이블명
   Group by 칼럼명;
   ```
   
   

