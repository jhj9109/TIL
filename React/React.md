# 2 React - JSX

1. #### DOM 요소 렌더링

   컴포넌트 내부는 하나의 DOM 트리 구조로 이루어져야 한다

   Why? => Vitual DOM에서 컴포넌트 변화를 감지할때 효율적인 비교를 위해서

   Vue : template => Fragment, 빈태그( <> ... </> ) 가능

2. #### JS 표현식 : **`{ }`** 사용

   <h1> Hello! {name} </h1>

3. #### 조건부 렌더링 : JSX내 if 사용 불가

   => JSX밖에서 if 문 활용 or 조건부연산자 (삼항연산자) 활용

   {name === '리액트' ? ( 리액트입니다. ) : ( 리액트가 아닙니다.) }

   {name === '리액트' ? ( 리액트입니다. ) : (null) }

   {name === '리액트' && ( 리액트입니다. ) }

   {값} => false or null or undefined 등은 렌더링 하지 않기 때문! (0은 아니다!)

   괄호로 감싸는 것은 필수 사항은 아니다!

4. #### return undefined 불가 => or 연산자 활용한 처리

   return name || '값이 undefined입니다.'

5. #### 인라인 스타일링

6. #### class 아닌 className

7. #### 태그는 꼭 닫아라 => <.../> : self-closing 태그

8. #### JSX내 주석 : {/* 활용, 예외 => 시작태그 여러줄 작성시 // ... 가능

9. #### Eslint : 문법 검사 도구, Prettier : 코드 스타일 자동 정리 도구

10. #### 선언

     const name = 'React'

     const => 변경 불가능한 상수 선언, 블록 scope

     let => 동적인 값을 담는 변수 선언, 블록 scope, => for문에서 활용

     var => ES6 이전, 함수 scope

11. #### Prettier

- 사용법 1 : `F1` => `format` 입력 후 `Enter` 

- 커스터 마이징

  - 프로젝트 루트 디렉토리에 ( `hello-react/` ) .	`.prettierrc` 파일 생성 후 작성

  - ```
    {
    	"singleQuote": true,
    	"semi": true,
    	"useTabs": false,
    	'tabWidth': 2
    }
    ```

  - [Prettier Options 페이지](https://prettier.io/docs/en/options.html) 참조

- 저장시 자동 코드 정리

  - `Code` (Window는 `File`) > `기본 설정` > `설정`
  - `format on save` 체크

12. #### 정리

- JSX는 HTML과 유사
- JSX는 코드로 보면 XML 형식이나 실제로는 `JS 객체` => 용도나 문법 상이