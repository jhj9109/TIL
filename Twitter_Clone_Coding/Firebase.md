# Firebase 시작

- Firebase Google 로그인

- 프로젝트 생성

  - 이름 설정
  - 구글 애널리틱스 사용 X

- 앱 등록

  - 이름 설정

  - Add Firebase SDK

    - `npm i --save firebase`

      - --save : 의존성 추가 옵션 => 실제론 입력하지 않아도 동일한 동작

    - src / firebase.js 생성

      - ES6 문법으로 import & export
      - 앱에서 firebase 시작 : `firebase.initializeApp(firebaseConfig)`

    - ```js
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

      