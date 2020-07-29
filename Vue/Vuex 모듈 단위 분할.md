# Vuex Store 모듈 단위 분할

- 스토어를 모듈로 분할
- 모듈은 최종적으로 스토어의 인스턴스로 병합
- 각 스테이트가 서로 충돌하지 않도록 하나의 트리구조로 합쳐짐

## 1. 네임스페이스 분할

> namespaced: true

| 분류 (예시)        | 분할 X                   | 분할 O                            |
| ------------------ | ------------------------ | --------------------------------- |
| state (value)      | store.state.모듈명.value | store.state.모듈명.value          |
| getter (upper)     | store.getters.upper      | store.getters[ '모듈명/upper' ]   |
| mutations (update) | store.commit('update')   | store.commit( '모듈명/update' )   |
| actions (update)   | store.dispatch('update') | store.dispatch( '모듈명/update' ) |

## 2. 모듈에서 전역 네임스페이스대상 접근

### getters

- 3, 4번째 인자로 접근
  - 게터명(state, getters, rootState, rootGetters)

### actions

- context로 전역접근
  - context.rootGetters.전역게터명
- 지역접근
  - context.getters.내모듈객체명

### commit & dispatch

- 3번째 인자로 전역접근
  - commit( '전역변이명', payload, { root : true })
  - dispatch( '전역액션명', payload, { root : true })
- 모듈접근
  - commit( '모듈명/지역변이명', payload)
  - dispatch( '모듈명/지역액션명')


## 3. 모듈화 올바른 이름 사용법

- map 핼퍼 사용시
  - `...mapActions('모듈명', [ '액션명', ..... ])`
- dispatch 사용시
  - `this.$store.dispatch('모듈명/액션명', 인자)`