# Before exam

1. ### 컨테이너

   1.시퀀스 : 스트링, 리스트, 튜플, 렌지

   2.언오더 : 셋, 딕트

1. ### 조건표현식 (Conditional Expresstion)

   참_값 if <조건식> else 거짓\_값

2. ### 리스트.index(값) : 해당값의 인덱스 리턴

   딕트.get()

3. ### 리스트 항목을 카운팅해서 키:값으로 만들기

   ```python
   my_dict = dict()
   for book in books:
       my_dict[book] = book_title.count(book)
   ```

4. ### 카운터해쉬

   ```python
   counter - {}
   for title in books:
       if title in counters:
           title_counter[title] += 1
       else:
           title_counter[title] = 1
   ```

7. ### continue : 지금 요소를 뛰어넘고 다음 요소로 진행 (ex: for문)
8. ### print( `함수.__doc__` ) : 함수 내 doc 출력
9. ### 기본값 인자 활용 뒤 기본값X 인자 사용 불가
10. ### 키워드 인자 활용 뒤 위치 인자 사용 불가
11. ### 가변인자리스트 *args : 튜플형태로 처리

12. ### 정의되지 않은 키워드인자 **kwagrs : 딕트형태로 처리

13. ### 몇가지 메소드

    1. .capitalize() : 앞글자

    2. .title(): `'`, 공백

    3. .upper()     .lower()       .swapcase()

    4. '값'.join(iterable) 

    5. .replace (old ,new , 갯수) 

    6. 스트링.find(x)

       스트링리스트.index(x) : 못찾으면 에러

       .get(key, default=None) : 키에러X ,

    7. .is : alpha, decimal, digit, numeric, space, upper, title, lower

    8. .append(x)

       .extend(iterable) : 원본변경

    9. .insert(idx, x)

    10. .remove(x) : 없으면 에러

        .pop(idx) : 리턴O

    11. .count(x)

    12. [::-1] 리버스 복사

    13. 리스트 컴프리핸션

        [식 **for** 변수 **in** iterable]

        [식 **for** 변수 **in** iterable **if** 조건식]

        [식 **for** 변수1 **in** iterable1 **for** 변수2 **in** iterable2] : 우선순위 : **for** 변수2 **in** iterable2

        [값1  **if** 조건식1 else 값2 if 조건식2 else 값3 **for** 변수 **in** iterable]

    14. 딕셔너리 메소드

        .pop (key , default) : key가 딕셔너리에 있으면 제거하며 값리턴, 없으면 default반환 

    15. 세트 메소드

        .add(elem) .remove(elem) .pop() .discard(elem) 에러 X 

        .update(*)

        .map(함수적용 , 이터러블) .zip(*이터러블) , filter(함수 True, 이터러블)
    