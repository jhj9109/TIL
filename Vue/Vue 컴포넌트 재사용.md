# 스켈레톤 코드 컴포넌트 리뷰

> Vue 컴포넌트 재사용을 위한 학습
>
> 사용자 입력 받는 Input을 컴포넌트로 만들고, 재사용하고자 함

## Input.vue

- `name`
  - input
- `props`
  - `inputvalue` => id & label의 for
  - `errorText` => 에러메시지
  - `password` => type : text or password
  - `placeholder` => placeholder
  - `label` => label명
  - `enterInput` => v-model역할을 한다. 바뀐 값을 Vue의 데이터에 반영한다.
  - `onEnter` => 내가 추가한 pros, @keyup.enter 에 바인딩 해줄 메서드
  - v-model와 props의 연동엔 실패
- `methods`
  - viewPassword()
    - `this.type = this.type==="password" ? "text" : "password";`
  - `changeInput($event, inputValue)`
    - `this.enterInput(event.target.value, type);`
    - `@input`에 바인딩
    - InputComponent의 값에 변화가 생기면, 값과 명칭을 인자로 넘기며 eventInput을 호출한다.
- `data`
  - `type`
    - `password`
  - `text`
    - ""

```vue
<template>
    <div class="input-with-label">

        <input v-model="text"
               :id="inputValue" :placeholder="placeholder"
               :class="{error : errorText.length > 0, complete : text.length > 0 && errorText.length === 0}"
               @input="changeInput($event, inputValue)"
               :type="password ? type :'text'"/>
        <label :for="inputValue">{{label}}</label>

        <div class="error-text" v-if="errorText.length>0">
            {{errorText}}
        </div>

        <span @click="viewPassword" v-if="password" :class="{active : type==='text'}" class="eyes-icon">
            <i class="fas fa-eye"></i>
        </span>
    </div>
</template>

<script>

    export default {
        name: "input",
        props : ['inputValue', 'errorText', 'password', 'placeholder', 'label', 'enterInput'],
        methods: {
            viewPassword() {
                this.type = this.type==="password" ? "text" : "password";
            },
            changeInput(event,type){
                this.enterInput(event.target.value, type);
            }
        },
        data: () => {
            return {
                type:"password",
                text:"",
            }
        },
    }
</script>
```

## 정리

- input의 모든 속성을 선언하고, 적절한 바인딩과 대입으로 재사용가능한 input 구현하였다.

- @input 역할이 상당히 크다.

- @keyup.enter은 키보드 동작을 위해 추가하였다.

  