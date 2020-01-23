# 명령어 약어 등록하기 

```shell
$ cd ~
$ vi .bashrc #$ code와 유사, vim 에디터 입력

#insert모드의 약자 i로 진입
alias jn="jupyter notebook" #jn이란 별명으로 변수 설정

#나오자~esc2 콜론 wq
$ cat .bash_history #그동안 사용한 코드 모두 볼수 있다
$ history #cat .bash_history와 같다

$ cd python
#설정 바꼇으니 이거 리로드 해줘
$ source ~/.bashrc
$ jn #jupyter notebook #실행, ctrl+c 종료

alias ssafy="git push origin master&& git push gub master"

```

- 주피터 단축키
- 방향치 좌h 우l 내려가기o
- vim-adventures.com

# Python

> 주피터노트북을 이용해 수업

## 저장

- **어떻게 : 연산자**
  -  `=`
- **무엇을  : 데이터타입(자료형)**
  - `숫자`
  - `글자`
  - `bool`(연산자)
- **어디에 : 변수/컨테이너**
  - `변수` 
  - `컨테이너형자료`
    - `시퀀스형` 
    - `비시퀀스형` 

## Ⅰ. Slicing

​		**파이썬은 모든 것이 객체화 되어있어서 생기는 특징**

- `[]`을 통해 접근, `[:]`을 통해 리스트를 슬라이싱할 수 있습니다.

- [시작:끝:간격] : ex) `[::3]` : 간격만 3으로 설정

  

- 단축평가 : 첫번째값이 확실할때, 두번째값은 확인하지 않음

- 글자에 적용되는것은 리스트에도 적용가능

- -5 ~ 256 까지의 id 동일 : 빈번하게 사용하는 값이므로 미리 값을 생성

  리스트는 mutable객체, 숫자자체는 immutable객체
  
  

## Ⅱ. 컨테이너형자료

> 순회가 가능하다 → for문등

### 	(1) tuple

- Immutable : 콤마 `,`를 사용하기 위해 내부적으로 사용하기 위한 역할
- LIst가 거의 모든 역할을 대체가능하기 때문에, List를 대신 쓴다

- 숫자 0이 6개 있는 list를 만들어 봅시다



## Ⅲ. 기타

- TDD : 테스트를 먼저 짜는방식 : 이후 파이썬 모듈파트에서 배울듯
- Git과 TDD 



### Ⅳ. 식과 문

#### 	 	1. 식 (expression)

- value(값) & operator(연산자)

- evaluate (연산자를 통한 값의 평가)

- 변수에 할당가능 (== 변수에 바인딩 가능)

  #### 2. 문 (statement)

- expression으로 구성

- 변수에 할당 불가능

- 세미콜론 포함 ( `:` )

- while : 조건 True동안 실행, 실행 종료조건 주어야함

- for :  정해진 횟수만큼 실행

  for i in range(10) : 순회때마다 새로운 값이 할당



#### 		3.조건 표현식(Conditional Expression)

- 조건문 : if 조건 : 수행1

- 조건표현식 : 수행1 if 조건 수행2

  ex) 변수 = 값1 if 조건 else 값2