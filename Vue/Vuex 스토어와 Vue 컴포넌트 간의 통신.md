# Vuex 스토어와 Vue 컴포넌트 간의 통신

## Ⅰ 컴포넌트에서 스토어 접근

### 1) this.$store 통해 접근

- `this.$store` 에는 루트 컴포넌트에 `store` 옵션으로 전달된 스토어 인스턴스가 존재
- 예시
  - `this.$store.commit('뮤테이션명', payload)`
  - `this.$sotre.state.count`

### 2) 헬퍼 함수를 사용해 접근

- 헬퍼함수 : mapState, mapGetters, mapMutations, mapActions
- 객체 스프레드 연산자나 Obkect.assign 함수와 함꼐 사용

- 예시

  - `...mapState([ '스테이트명' ])`
  - `...mapState({ 로컬참조명 : '스테이트명' })`

- 네임스페이스 적용된 모듈은 네임스페이스 문자열을 헬퍼 함수의 첫번째 인자로 전달 가능

  - `...mapState('모듈명', [ '스테이트명' ])`

    ```
    import {createNamespaceHelpers} from 'vuex'
    
    //const 모듈명Helpers = craetenamespaceHelpers('모듈명')
    const counterHelpers = craetenamespaceHelpers('counter')
    
    ...
    
    counterHelpers.mapSate(['스테이트명'])
    ```

    

## Ⅱ 스토어에 접근하는 컴포넌트를 최대한 적게 유지하기

- 스토어에 접근하는 컴포넌트를 제한하도록, 규칙을 설정
- 프레젠케이션 컴포넌트, 컨테이너 컴포넌트 두 종류로 나누는 방법
- 아토믹 디자인과 같이 분류하는 방법

### 1) 프레젠테이션 컴포넌트

- 외관을 나타내는 컴포넌트
- No 스토어 접근
- No 외부 API 요청
- 컨테이너 컴포넌트에 이벤트 전달 / props를 받을 수만 있다

### 2) 컨테이너 컴포넌트

- 동작에 초첨
- 스토어에 액션을 실행하거나 스토어에서 데이터를 읽어온다.

### 3) 아토믹 디자인 적용



## Ⅲ Vuex와 Vue Router 연동하기

### 1) vuex-router-sync 설치

```
npm install vuex-router-sync
```

### 2) 라우터와 스토어 동기화

```
//main.js
import { sync } from 'vuex-router-sync'

//라우터와 스토어 동기화
sync(store, router)

// stroe.state.route 아래에 라우팅 데이터를 저장
```

### 3) 게터, 액션 => rootState를 통해 라우팅 데이터 접근

- 3번째 인자로 `rootState`
- URL주소에 포함된 id 접근 : `rootState.route.params.params.id`

- router-link 대신 액션의 라우터 인스턴스를 사용 가능
  - `commit('setSearchResult', result)`
    - setSearchResult(state, result) { state.result = result }
  - `router.push('/search')`

