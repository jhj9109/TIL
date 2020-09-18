# 프로젝트 초기 구조 잡기

- components 와 routes 디렉토리 생성
- react-router-dom 설치

## Components

- App.js => index.js의 App import 시 경로 같이 수정
- Router.js
- 

# routes

- Home.js
- Auth.js
- Profile.js
- Edit Profile.js



## react-router-dom

- 설치 ` npm install react-router-dom`



## npm 오류 임시 해결

> Cannot read property "match" of undefined

- 참고 : https://dev.to/stephencweiss/npm-cannot-read-property-match-of-undefined-238n
  1. Delete `node_modules` *and* `package-lock.json`
  2. Run `npm install` again



## Router.js

- react-router-dom 에서 필요한 요소들 import
  - HashRouter as Router
  - Route
    - path랑 바인딩
    - exact 키워드 : 정확한 주소값 사용
  - Switch
    - 라우팅시 분기할때 활용

- Fragment `<> </>`  : 부모 요소 없이 여러 요소를 사용하고 싶을때 활용
- `const [isLoggedIN, setLoggedIn] = useState(false)`
  - 로그인 여부 T / F
  - 초기값은 false 
  - 한 가지 역할만 하도록 App.js로 이동
  - `const AppRouter = ({ isLoggedIn }) =>`

## App.js

- `const [isLoggedIN, setLoggedIn] = useState(false)`
- `<AppRouter isLoggedIn={isLoggedIn} />` 

# Absolute imports

- root 경로에 jsconfig.json 파일을 생성한다.

- baseUrl을 `src/` 로 설정하는 옵션을 작성한다.

  ```json
  {
      "compilerOptions": {
          "baseUrl": "src"
      },
      "include": ["src"]
  }
  ```