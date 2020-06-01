# Live 1

저번주

- 단일 페이지내에서 비동기식 요청과 반영
- ES6 : jquery도 필요없는 시대

## 1. Vue.js

> made by Evan You
>
> 구글의 FE 프레임워크 Angular 사용 > 무거운 개념 덜어내기

### 1.1 What

- Front-End Framework
  - FE : Clinet-side : UI
- SPA 제작
  - 1회차 빅데이터, 비동기 요청 갱신
- Client-side rendering
  - DTL > HTML 변환 : 기존 - 서버측에서 만들고 던진다
  - 서버측에서 던지고 ,브라우저가 받아서 만든다(==JS)
- MVVM 패턴 (Model, View, ViewModel)
  - Model : Plain JS Objects `{key:value}`
  - View : DOM `HTML`
  - VM(Dom Listeners, Directives) : Vue `???`

- Reative / Declarative(선언형)
  - Facebook의 React
  - 하나의 레코드에 따른 수많은 데이터 갱신 대응

### 1.2 Why

- 배우기 쉽다
- $
- UX 향상
- 프레임워크 (프렌차이즈)의 장점 (DX 향상)
  - No etc, 선택과 집중
  - 유지/보수 용이
  - 커뮤니티와 라이브러리

### 1.3 How

초기 세팅

- VScode : Vetur 설치
- 크롬익스텐션 : Devtools 설치 * 파일 URL엑세스 허용
- CDN

데이터 반응 뷰

# 1. Live 1 무한스크롤 만들기1

## 1.1 펑션키워드와 애로우펑션 사용하는때

- CB는 애로우 펑션

## 1.2 더미데이터

 jsonplaceholder

## 1.3 페이지네이터

jsonplaceholder > json.server (jsonplaceholder powered by json.server)

- `...?_page=1`
- 핵심 : 데이터를 분할해서 보낼 수 있어야 한다.

## 1.4 extends 비교

>  measurethat.net

- concat `var other = arr.concat(params)` : 6,511,812 
- spread operator `var other = [1,2, ...params]` : 47,920,640
- push `var other = arr.push(...params)` : 33,835,700

## 1.5 life cycle hook

- 끼어들수 있는 시점
  - created
  - mounted
  - updated

## 1.6 scrollmonitor

- 무한 스크롤

## 1.7 바텀이 위에 천장에 붙었어요 !!!

- DOM 조작은 mounted 시에 제대로 동작한다.

# 2. Zoom1

## 2.1 어제 로또 터진문제

- Same Origin Policy
  - For 안정적 운영
  - 같은 서버 리소스(원천)
- 반대 => Cross Origin Policy

- 결론
  - Browser (JS) Axios 요청을 통해 CORS 관련 에러가 나면 우리가 할 수 있는게 없다.
- HTML 페이지가 로드된 시점에 Request Header 근본 없는 페이지...
- 서버 구동 > Origin을 갖게된다. > 된다.
- 장고 > 장고CORS가 해결해준다.

## 2.2 라이브 내용은 뭐였을까?

- Life Cycle Hook

  - 왜 알아야 할까?
    - 클라이언트 렌더링

- Declarative (선언형)

  - 유산슬을 만들어줘(대신해서 절차를 수행해줄 누군가가 필요하다 > Framework)

  - Vue.js (데이터의 변화에 맞춰 UI를 변경)

  - UI 단계(Hook)

    == url('articles') => views (list_articles())

    == JS코드가 처음 생성됐을때 (Hook) => function

    - 자주 쓰는것 : 컴포넌트가 .... 할때

- Imperative (명령형, 절차적)

  - 직접 요리 (언제 무엇을)
  - 레시피
  - Vanilla JS(DOM, 이벤트리스너)

# 3. Live 2 무한스크롤 만들기2

## 3.1 타이밍

- mounted

## 3.2 비동기 2가지

- axios
- `setTimeout( () => {}, 시간)`

## 3.3 스크롤

- `window.scroll(0, 0)`
- `scroll(0, 0)`
- scrollMonitor
  - 밀어내기 > updated > `isFullyInViewport`

## 3.4 return

- 조회만 하고싶을때 == Read

- computed : 데이터를 CUD 하지 않고 READ하고 싶을때
- computed는 캐싱을 지원한다.

```python
@property
def gravatar_url:
	return ....

user.gravatar_url // 실행아닌 값으로 사용
```

# 4 Zoom2

## 4.1 체크박스

- v-model과 연결
- `:class=""{ 값: t/f, 값: t/f}"` > `@click=check(todo)` 대체
- v-for에서 생기는 문제 > `:key` 넣기 > 실제 DB의 id가 등록되니 괜춘

- [각 키의 code mapping 볼 수 있는 사이트](keycode.info)

## 4.2 기타등등

- `@click="값 = !값"` : 같이 간단한 JS 문법 비스무리한것 가능

- 캐싱 :`computed`는 불려진 값이 바뀔때만 업데이트한다.

- watch (angular)
  - 데이터를 변화를 지켜보는 hook
  - 특정 데이터가 변화되었을때, 데이터 변경 & 렌더링
  - imperative(명령형)
- computed
  - 데이터 변화를 지켜보지 않고
  - 프레임워크가 데이터가 변화하였을때, 데이터 변경 & 렌더링
  - declarative(선언형)
- watch 로 쓰면 직접 짜야되는거를 computed 에서는 프레임워크가 해준다는 거에요?

- f() => 리턴 => ++ (값의 변화) =>  

# 1. LIVE1

서론

- HTML 한장 => 길어진다 => Vue CLI 환경

## node

- JS 환경 제공
- version : 12.16.3 LTS 사용 => 5.27일부로 12.17.0 LTS 등장
- npm (6.14.4) == 파이썬의 pip

```
$ npm install -g @vue/cli
```

- `-g` : 글로벌 => 정해져있다 (설치 문서에 안내되어있는것만)

## vue CLI

- vue CLI == django
- vue

```
vue create 03_first-vue-cli
please pick a preset => default / manual

cd 03_first-vue-cli
npm rum serve

App running at:
  - Local:   http://localhost:8080/ => click
  - Network: http://192.168.219.178:8080/
```

```vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <hr>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Happy Hacking"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default { // object
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

- tmplate / script / style
- export를 써야 import가 가능

컴포넌트 사용법

- 1. import ```import 이름 from 경로```
  2. 등록한다 ```components: { 이름 }```
  3. HTML 작성 ```<이름><이름/>```

- `< + tab` : 자동 구조화
- The template root requires exactly one element

패키지 설치

- npm i 패키지이름

빌딩

- npm run build
- root 기준 => 배포기준 => `serve -s dist/`

장고는 : 분업

Vuejs : 합일 => 분리작성 => 편하라고 (Component 단위)

dist : distributable

정리

- 컴포넌트 =>  합일 => SPA

# 2 Zoom

- 바벨 => JS를 브라우저에 맞게

내용

- JS for 브라우저 => 모듈화 Nob => Module Bundler 등장
- Webpack ㄷㄷㄷㅈ
- Bundled Page의 유리함
  
  - HTTP => static 파일은 하나로 전달되는것이 경제적, 안정적
- 모듈 == 컴포넌트 == vue.js 

- angular (MVC)
  - M : 데이터
  - V(T) : UI
  - C : 데이터 <=> UI
- react (Component Based Architecture)
  
- 눈에보이는 그대로 => FE 개발팀 변화 => Component 중심 개발팀
  
- SFC : Single File Component

- Vue CLI => SFC Vue App

  ​	0. 컴포넌트 생성 (index.vue)

  1. 불러온다
  2. 등록한다.
  3. 사용한다.

# 3. Live 2

- SPA인데 url 꾸미기
- 즉, url에 따른 다른 컴포넌트 렌더링
  - `/` => index
  - `/lotto` => lotto
- `vue add router` => 이거 하기전에 커밋하지 않으면 후회해? : y => 히스토리 쓸래? : y
  - data / route / 여러 정보 => 잘 사용하면 되겠다!
  - 히스토리 : 뒤로가기

- `to="url주소"` => index.js의 path 정의된 파트가 받는다.
  - path는 `url주소` 이고  name은 `컴포넌트이름`이야 컴포넌트는 `component: () => import('컴포넌트경로')` 로 가면 돼

- 흐름
  - App.vue의 ``<router-link to="/경로"/>` 
  - index.js의 `Vue.use(VueRouter) routes = [ path: ... , name : ... , component : .... ]` => 여기 컴포넌트는 뷰스's
  - 뷰스.vue의 `export default { components: { ... }}`
  - 컴포넌트.vue ....

- views == pages => 라우터의 맵핑 받은 자

베리어블 라우팅

- `/hello/:name` : data > $route > params > {name: "...."}
  - => `this.$route.params.name`

막판정리

- 1url <=> 1component
  - 요청을 실제로 다시 보내는것 아닌
  - 이미 가진것들로 SPA가 실행해 반환
- Vue (SPA)의 redirect
  - `this.$router.push( { name: 'path네임', query: { 키: 값 }})`
  - ```this.$router.push(`/path네임?키=${this.data변수}`)```

- 잊지말자! views의 아그들은 url을 하사받은 간택받은자들이다!

# 4. Zoom 2

- window.history
- window.location

import vs require

- `import _ from 'loadash'` => CS6
- `var _ = require('loadash')`

- 바벨 => 브라우저마다 쓰는 언어 통일 / 변환

[CommonJS](https://d2.naver.com/helloworld/12864)

- 서버사이드 JS 주요 쟁점
  - 서로 호환되는 표준 라이브러리가 없다.
  - 데이터베이스에 연결할 수 있는 표준 인터페이스가 없다.
  - 다른 모듈을 삽입하는 표준적인 방법이 없다.
  - 코드를 패키징해서 배포하고 설치하는 방법이 필요하다.
  - 의존성 문제까지 해결하는 공통 패키지 모듈 저장소가 필요하다.

- 모듈화
  - 스코프(Scope): 모든 모듈은 자신만의 독립적인 실행 영역이 있어야 한다.
  - 정의(Definition): 모듈 정의는 exports 객체를 이용한다.
  - 사용(Usage): 모듈 사용은 require 함수를 이용한다.
  - 변수 파일마다 독립 스코프 & `exports.메소드 = fuction () {}`  => `var a = require("파일명")` & `a.메소드`
  - 

# 자습

```bash
$vue create 04_ex
$vue add router
```

