# SPA와 Vue Router

> 0728 작성

## SPA 구현에 필요한 기능들

- 클라이언트 사이드에서 히스토리 관리하는 페이지 이동
- 비동기로 데이터 받아오기
- 뷰 렌더링
- 모듈화된 코드 관리

## Vue Router

- SPA 구현하기 위한 기능들을 제공한다.
- 기본 페이지 이동
- 중첩 라우팅
- 리다이렉션과 엘리어싱
  - 리다이렉션 : URL 변경
  - 엘리어싱 : URL 변경 없이 라우팅 처리만 실행
- HTML History API와 URL 해시를 이용한 히스토리 관리 (IE9에서는 자동으로 풀백)
- 자동으로 CSS 클래스가 활성화되는 링크 기능
- Vue.js 트랜지션 기능을 이용한 페이지 이동 트랜지션
- 커스터마이즈된 스크롤링

## 기초 라우팅

### 라우트 설정

```
// routes, 배열로 전달
[
  {
    path: '/url',
    name: 'urlName',
    component: 'componentName'
  }
  ...
]
```

```
const router = new VueRouter({
	routes
})
```

```
new Vue({
	router: router
}).$mount('#app')
```

```html
<router-link to="/url"> 멘트 </router-link>
```

### 패턴 매칭

- path의 url 주소에 `:` 를 붙여 패턴 작성
- `path: 'user/:userId'`
- `{{ $route.params.userId }}`

```html
<router-link :to="{ name: 'url명', params: '키: 밸류, userId: 3395'}"> 멘트 </router-link>
```

```
router.push({ name: 'url명', params: { 키 : 밸류})
```

### 훅 함수

- 페이지 이동 전후 시점에 추가 처리를 삽입할 수 있는 훅 함수를 제공
- 리다이렉트나 페이지 이동 전 사용자 확인 등 구현에 활용
- 전역 훅 함수, 라우트 단위 훅 함수, 컴포넌트 내 훅 함수

#### 전역 훅 함수

- router.beforEach
- to : 현재 페이지 정보
- from : 이동 대상 페이지 정보

```
router.beforeEach(function(to, from, next) {
	// 에제 : 사용자 목록 페이지로 접혹하면 /top으로 리다이렉트
	if (to.path === '/users') {
		next('/top')
	} else {
		// 인자 없이 next를 호출하면 일반적인 페이지 이동
		next()
	}
})
```

#### 라우트 단위 훅 함수

- 라우트에 같이 정의

```
path: ... ,
component: ... ,
beforeEnter: function(to, from, next) {
	// /users?redirect-true로 접근할 때만 top으로 리다이렉트하는 훅 함수를 추가함
	if (to.query.redirect === 'true') {
		next('/top')
	} else {
		next()
	}
}
```

#### 컴포넌트 내 훅 함수

```
data() {
	return {
    ...
  },
  // 페이지는 이동되었으나 컴포넌트가 초기화되기 전에 호출된다
  // 다음페이지로 이동하며 컴포넌트가 사라질때 실행되는 beforeRouteLeave로 있다
  beforeRouteEnter: function(to, from, next) {
  	getUsers((function(err, users) {
  		if(err) {
  			this.error = err.toString()
  		} else {
  			// next로 전달된는 콜백함수로 자기 자신에 접근한다.
  			next(function(vm) {
  				vm.users = users
  			})
  		}
  	}).bind(this))
  	// Function.prototype.bind는 this의 유효범위 전달하기 위해 사용
  },
  // $route의 변경을 모니터링하며 라우팅이 수정되면 데이터를 다시 받아옴
  watch: {
  	'$route': 'fetchData'
  }
}
```

## 활용 예

- 로그인 페이지 접근

  - 로그인 상태 : 메인 페이지로 리다이렉트
  - 비로그인 상태 : 그대로

- 로그인이 필요한 페이지로 접근

  - 로그인 상태 : 그대로
  - 비로그인 상태 : 로그인 페이지로 리다이렉트
    - 맞춤 메시지 `<p v-if-"$route.query.redirect"> 로그인이 필요합니다 </p>`
    - 로그인 이후 리다이렉트 : `this.$route.replace(this.$route.query.redirect || '/')`

- 로그아웃

  ```
  path: '/logout',
  beforeEnter: function(to, from, next) {
  	//logout()
  	next('/')
  }
  ```

  

## 로컬 스토리지에 token 저장

- `localStorage.token = 토큰정보`
- 로그아웃 : `delete localStorage.token`
- 로그인상태 : `!!localStorage.token`

### 로그인 페이지로 보내며 리다이렉트 추가

```
function(to, from, next) {
	next({
		path : '/url주소',
		query: {
			redirect: to.fullPath
		}
	})
}
```



## Router 인스턴스와 Route 객체

### $router와 $route

- $router : Router 인스턴스를 가리킴
  - Router란
    - 웹 앱 전체에서 하나만 존재
    - 전반적인 라우터 기능 관리
    - 히스토리 관리
    - router-link 요소 없이 페이지 이동시 사용한다
- $route : Route 객체를 가리킴
  - Route란
    - (페이지 이동등으로) 라우팅 발생시마다 생성되는 객체
    - 현재 활성화된 라우트의 상태를 저장한 객체
    - 현재의 경로 및 URL 파라미터 정보가 담긴 객체
    - 컴포넌트 내부 구현 Router 훅 함수 들을 통해서도 참조 가능
    - watch에서 모니터링

### Router 객체의 주요 프로퍼티와 메서드

| 프로퍼티 / 메서드                        | 설명                                                         |
| ---------------------------------------- | ------------------------------------------------------------ |
| app                                      | 라우터를 사용하는 루트 Vue 인스턴스                          |
| mode                                     | 라우터 모드(히스토리 관리와 함께 설명함)                     |
| currentRoute                             | 현재 라우트에 대한 Route 객체                                |
| push(location, onComplete?, onAbort?)    | 페이지 이동 실행, 히스토리에 새 엔트리를 추가하고 브라우저에서 뒤로가기 버튼이 눌리면 앞의 URL로 돌아감 |
| replace(location, onComplete?, onAbort?) | 페이지 이동 실행, 히스토리에 새 엔트리 추가하지 않음         |
| go(n)                                    | 히스토리 단계에서 n단계 이동 window.history.go(n)과 비슷     |
| back()                                   | 히스토리에서 한 단계 돌아감 history.back()과 같음            |
| forward()                                | 히스토리에서 한 단계 앞으로 나아감                           |
| addRoutes(routes)                        | 라우터에 동적으로 라우트를 추가                              |

### Route 객체의 주요 프로퍼티

| 프로퍼티 | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| path     | 현재 라우트의 경로를 나타내는 문자열                         |
| params   | 정의된 URL 패턴과 일치하는 파라미터의 키-값 쌍을 담고 잇는 객체, 파라미터가 없다면 빈 객체 |
| query    | 쿼리 문자열의 키-값 쌍을 담고 있는 객체, 쿼리가 없다면 빈 객체. 경로가 /foo?user=1이면  $route.query.user == 1이 된다. |
| hash     | 현재 URL에 URL 해시가 있을 경우 라우트의 해시값을 찾는다. 해시가 없다면 빈 객체 |
| fullPath | 퀴리 및 해시를 포함하는 전체 URL                             |
| name     | 이름을 가진 라우트인 경우 라우트의 이름                      |

- [hash](https://developer.mozilla.org/ko/docs/Web/API/URL/hash) : `#` 와 함께 URL 프래그먼트 식별자를 담고 있는 [USVString](https://developer.mozilla.org/ko/docs/Web/API/USVString)

## 중첩라우팅

> 어떤 컴포넌트 안에 든 컴포넌트에 대한 라우트 정의

```
path: '/user/:userId'
name: 'user'
component: User,
children: [
	{
    // User 컴포넌트 안의 <router-view> 안에서 렌더링 됨
    path: 'profile',
    component: UserProfile
	},
	{
		...
	},
]
```

## 리다이렉션과 앨리어싱

- URL 변경하는 리다이렉션, URL 변경 없이 라우팅 처리하는 앨리어싱

### 리다이렉션

```
{path: '/notfound', component: NotFound},
{path: '*', redirect: '/notfound'}
```

### 앨리어싱

```
{ path: '/a', component: A, alias: '/b' },
{ path: '/c', component: C, alias: ['/d', '/e'] }
```

- `/b`에 접근시 `/a`로 렌더링
- `/d` 나 `/e` 에 접근시 `/c` 로 렌더링

## 히스토리 관리

- SPA는 서버사이드 라우팅을 거치지 않음
- 브라우저 히스토리를 클라이언트에서 관리
- URL 해시, HTML5 History API 사용하는 방법

### URL 해시

- `#` 를 붙여 라우팅경로 관리
- 사용자가 직접 브라우저에 URL을 입력해도 따로 특별한 처리가 필요하지 않다

## HTML5 History API

- `#`를 붙이지 않아도 됌
- 사용자가 직접 브라우저에 URL 입력해 접근하는 경우에 대한 SPA 페이지를 적절히 반환해줘야 한다
- Vue router 인스턴스 옵션 객체의 `mode` 속성을 `history`로 설정하면 된다. (`main.js`에 작성되어 있다)

## vuex-router-sync

- vuex 연동 가능
- 현재 라우팅 정보를 Vuex에서 관리
  - 컴포넌트와 라우팅 상태를 한곳에서 관리