# Firebase 시작

## Firebase Google 로그인

## 프로젝트 생성

- 이름 설정
- 구글 애널리틱스 사용 X

## 앱 등록

-   이름 설정

- Add Firebase SDK

  - `npm i --save firebase`

    - --save : 의존성 추가 옵션 => 실제론 입력하지 않아도 동일한 동작

  - src / firebase.js 생성

    - ES6 문법으로 import & export
    - 앱에서 firebase 시작 : `firebase.initializeApp(firebaseConfig)`

    ```js
    import * as firebase from "firebase/app"
    
    const firebaseConfig = {
        apiKey: "AIzaSyCaiX3_Gt_9ql-peIENra7nfV7OXZZUZq0",
        authDomain: "clonig-twitter.firebaseapp.com",
        databaseURL: "https://clonig-twitter.firebaseio.com",
        projectId: "clonig-twitter",
        storageBucket: "clonig-twitter.appspot.com",
        messagingSenderId: "759296892824",
        appId: "1:759296892824:web:4cbbe1a1eab4c5b427d5ed"
    };
    
    export defalut firebase.initializeApp(firebaseConfig);
    ```

## .env 설정

> env 파일은 프로젝트 최상위 루트에 있어야함!

- 이 과정은 보안을 위한 과정은 아님

  - build시 실제 값들로 변환되기 때문
  - 특정사이트에서만 이 key들을 사용할 수 있음 => 나중에!

- 단, github등에 올라가는 것을 방지하기 위한 수단!

- src / firebase.js

  ```js
  import * as firebase from "firebase/app"
  
  const firebaseConfig = {
      apiKey: process.env.REACT_APP_API_KEY,
      authDomain: process.env.REACT_APP_AUTH_DOMAIN,
      databaseURL: process.env.REACT_APP_DATABASE_URL,
      projectId: process.env.REACT_APP_PROJECT_ID,
      storageBucket: process.env.REACT_APP_STORAGE_BUCKET,
      messagingSenderId: process.env.REACT_APP_MESSAGIN_ID,
      appId: process.env.REACT_APP_APP_ID,
  };
  
  export defalut firebase.initializeApp(firebaseConfig);
  ```

- .env

  ```
  REACT_APP_API_KEY=값
  REACT_APP_AUTH_DOMAIN=값
  REACT_APP_DATABASE_URL=값
  REACT_APP_PROJECT_ID=값
  REACT_APP_STORAGE_BUCKET=값
  REACT_APP_MESSAGIN_ID=값
  REACT_APP_APP_ID=값
  ```

## auth 서비스 호출

- firebase.js => fbase.js 에서 다음과 같이 auth를 호출하여 export 한다.

  ```react
  ...
  firebase.initializeApp(firebaseConfig);
  export const authService = firebase.auth();
  ```

  

### 현재 로그인한 유저

> authService.currentUser