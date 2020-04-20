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

- **추가** :**INSERT INTO** table_name (col_name, ...) **VALUES** (<val1>, ...);
  - **INSERT INTO** table_name **VALUES** (col_val, ...);
    - 모든 열에 데이터를 넣을 때에는 col_name 명시 불필요
- **조회** : **SELECT** col_name **FROM** table_name **WHERE** conditions;
- **수정** : **UPDATE** table_name **SET** <col1=val1,...> **WHERE** conditions;
- **삭제** : **DELETE** FROM table_name **WHERE** conditions;
- SELECT<col>
  - DISTINCT<col> : 중복 없이
  - COUNT<col> : 
    - AVG, SUM, MAX, MIN
- FROM <table> 
- WHERE <condition1> AND<cond2>
  - LIKE <col> '구문'
- GROUP BY <col>
- ORDER BY <col> [ASC/DESC]
  - ASC(default) : 오름차순
  - DESC : 내림차순
  - 다수 : 왼족부터
- LIMIT <integer>
  - LIMIT <integer> OFFSET <integer>
- ;

아아

와일드 카드

- % : 문자열이 있을 수도 있다.
- _ : 반드시 한 개의 문자가 있다.

<col>_without_schema

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