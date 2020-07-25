# Computed vs Watch

>https://kr.vuejs.org/v2/guide/computed.html0

## Computed

- 선언형

- 의존성 파악 => 대상이 변할때만 재계산 => 캐싱

  - 단, Date.now()처럼 의존성없는 대상만 있다면, 원하는 대로 재계산 되지 못함!

- 예제코드

  - get : 일반적인 getters
  - set : `vm.fullName = '새로운 이름'` 실행하면, setter가 호출, vm.firstName과 vm.lastName 가 업데이트 된다.

  ```vue
  <script>
    var vm = new Vue({
    el: '#demo',
    data: {
      firstName: 'Foo',
      lastName: 'Bar'
    },
    computed: {
      fullName: {
          get: function () {
            return this.firstName + ' ' + this.lastName
          },
          set: function (newValue) {
        	  var names = newValue.split(' ')
            this.firstName = names[0]
            this.lastName = names[names.length - 1]
    		}
      }
    }
    })
  </script>
  ```

  

## Watch

- 명령형

- 캐싱 X

- 예제 코드

  ```vue
  <script>
    var vm = new Vue({
    el: '#demo',
    data: {
      firstName: 'Foo',
      lastName: 'Bar',
      fullName: 'Foo Bar'
    },
    watch: {
      firstName: function (val) {
        this.fullName = val + ' ' + this.lastName
      },
      lastName: function (val) {
        this.fullName = this.firstName + ' ' + val
      }
    }
  })
  </script>
  ```

  

## Watch 속성 사용이 더 적합할때

- 데이터 변경에 대한 응답으로, **비동기식** or **긴 소요시간의 작업 수행**시 적합
- 예제

```vue
<template>
  <div id="watch-example">
    <p>
      yes/no 질문을 물어보세요:
      <input v-model="question">
    </p>
    <p>{{ answer }}</p>
  </div>
</template>

<script src="https://unpkg.com/axios@0.12.0/dist/axios.min.js"></script>
<script src="https://unpkg.com/lodash@4.13.1/lodash.min.js"></script>

<script>
	var watchExampleVM = new Vue({
	el: '#watch-example',
	data: {
			question: '',
			answer: '질문을 하기 전까지는 대답할 수 없습니다.'
	},
	watch: {
			// 질문이 변경될 때 마다 이 기능이 실행됩니다.
			question: function (newQuestion) {
			this.answer = '입력을 기다리는 중...'
			this.debouncedGetAnswer()
			}
	},
	created: function () {
			// _.debounce는 lodash가 제공하는 기능으로
			// 특히 시간이 많이 소요되는 작업을 실행할 수 있는 빈도를 제한합니다.
			// 이 경우, 우리는 yesno.wtf/api 에 액세스 하는 빈도를 제한하고,
			// 사용자가 ajax요청을 하기 전에 타이핑을 완전히 마칠 때까지 기다리길 바랍니다.
			// _.debounce 함수(또는 이와 유사한 _.throttle)에 대한
			// 자세한 내용을 보려면 https://lodash.com/docs#debounce 를 방문하세요.
			this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)
	},
	methods: {
			getAnswer: function () {
			if (this.question.indexOf('?') === -1) {
					this.answer = '질문에는 일반적으로 물음표가 포함 됩니다. ;-)'
					return
			}
			this.answer = '생각중...'
			var vm = this
			axios.get('https://yesno.wtf/api')
					.then(function (response) {
					vm.answer = _.capitalize(response.data.answer)
					})
					.catch(function (error) {
					vm.answer = '에러! API 요청에 오류가 있습니다. ' + error
					})
			}
	}
	})
</script>
```

