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

# 3 React - Component

## 3.1 클래스형 컴포넌트

- state 및 라이프사이클 기능 사용 가능 => (함수형의 단점) : v16.8 Hooks 기능 도입으로 해결
- 임의 메서드 정의 가능
- render 함수가 반드시 필요!

```react
// 함수형
functjion App() {
	const name = 'React';
	return ...
}
```



```react
import { Component } from 'react';
class App extends Component {
	render() {
		const name = 'React';
		return ...
	}
}
```

## 3.2 컴포넌트 생성

#### ES6 화살표 함수

- 일반 함수 : this 가 자신이 종속된 객체를 가리킴
- 화살표 함수 : 자신이 종속된 인스턴스를 가리킴
  - 값을 연산하여 바로 반환해야할 때 사용하면 가독성 높임

#### Reactjs Code Snippet

- rsc : 함수형 컴포넌트
- roc : 클래스형 컴포넌트

#### export & import

- `export default MyComponent` : 다른 파일에서 import 시 선언 된 MyComponent를 불러옴

## 3.3 props

- properties 줄임말
- 사용법
  - at 부모 : `<MyComponent name="값">` 
  - at 자식 :
    - `const MyConponent = props => { return <div> {props.name}</div>}`
    - `{ }` 기호를 활용하여 `{props.name}` 로 사용
  - 없으면 undefined 일듯?
- 기본값 지정
  - at 자식 : `MyComponent.defaultProps = { name: '기본값'}`
- 태그 사이의 내용 보여주기
  - at 부모 : <MyComponent>보여줄값</MyComponent>
  - at 자식 : `{ props.children }`

- 비구조화 할당 (destructuring assignment) : props 계속 붙여 사용하는것 보완
  - `const { name, children } = props;`
  - 객체형태 : `const MyConponent = ({name, chidren}) => { return <div> {props.name}</div>}`

- `propTypes` 통한 props 검증
  - `import PropTypes from 'prop-types'`
  - `MyComponent.propTypes = { name: PropTypes.string }` => 타입 오류
  - 타입 오류시 : 출력은 되나 console 경고문 출력됨
  - `isRequired` : `PropTypes.string.isRequired`  => 미지정 오류

- PropTypes 종류 : https://github.com/facebook/prop-types 에서 확인 가능

## 3.4 State

> 함수형 컴포넌트 : useState 함수를 통해 사용

- state : 컴포넌트 내부에서 바뀔 수 있는 값
- props: 컴포넌트에서는 읽기 전용, 부모에서 바꿔줘야함

### 함수형 컴포넌트

> Hooks( useState, ... ) 사용

배열 비구조화

- const [one, two] = [1, 2];

useState 사용

- ```react
  import React, { useState } from 'react';
  
  const Say = () => {
  	const [msg, setMsg] = useState('');//'': 초기값
      // 배열1(msg):현재 상태, 배열2(setMsg): 상태를 바꾸어 주는 함수
  	const onClickEnter = () => setMsg('안녕하세요!');
  	const onClickLeave = () => serMsg('안녕히 가세요!');
  }
  ```

- 한 컴포넌트에서 여러번 사용 가능

state 사용시 주의 사항

- `state` 값의 변경은 `useState`를 통해 전달받은 세터 함수를 사용해야 한다.

- **객체 or 배열의 업데이트**

  - 사본을 만든다 => 사본을 업데이트 한다 => 사본을 세터 함수에 넣어 업데이트 한다

  - ```react
    const obj = {a:1, b:2, c:3}
    const nextObj = {...obj, b: 2} // 사본 생성 후 b값만 덮어 쓰기
    ```

  - ```react
    const arr = [{id:1, value:true}, {id:2, value:false}];
    let nextArr = arr.concat({id: 4})ㅣ // 새 항목 추가
    nextArr.filter(item => item.id !== 2) // id 2인 항목 제거
    nextArr.map(item => (item.id === 1 ? { ...item, value:false } : item))
    // id 1인 항목 value를 false로 설정
    ```

  - **객체 사본**은 **spread 연산자 `...`** 를 사용

  - **배열에 대한 사본**은 **배열의 내장 함수** 활용

정리

- Vue의 props emit
  - props : 부모 state => 자식 props
  - emit : 부모 컴포넌트의 메서드 호출

# 4 React - 이벤트 핸들링

- Event : `사용자` 가 `웹 브라우저` 에서 `DOM` 요소들과 상호작용 하는 것
- HTML에서의 Event : `이벤트명="실행할 JS 코드"`

## 4.1 React의 이벤트 시스템

- 주의 사항
  -  `카멜` 표기법 작성
  -  함수 형태의 객체 전달
  -  DOM 요소에만 이벤트 설정 가능
     - 컴포넌트에 이벤트 자체적으로 설정 불가
     - 자식 컴포넌트에서 내부의 DOM 이벤트로 전달 받은 props로 설정은 가능
- 이벤트 종류
  - Cliboard
  - Composition
  - Keyboard
  - Focus
  - Form
  - Mouse
  - Selection
  - Touch
  - UI
  - Wheel
  - Media
  - Image
  - Animation
  - Transition
  - 나머지는 [리액트 매뉴얼](https://facebook.com/github.io/react/docs/events.html) 참조

## 4.2 예제로 이벤트 핸들링 익히기

- e : SyntheticEvent 로, 웹브라우저의 네이티브 이벤트를 감싸는 객체
- 이벤트 종류 후 초기화 되므로 비동기적으로 참조할 일이 있다면 `e.persist()` 호출
- 방식
  - 렌더링 메서드 내부에 함수를 정의 => 컴포넌트 매핑시 더 편리하기도 함
  - 임의 메서드 만들기
- 객체 안에서 key를 `[ ]`로 감싸면 그 안에 넣은 레퍼런스가 가리키는 실제 값이 key 값이 됨
  - `[e.target.name]` : value 

## 4.3 함수형 컴포넌트로 구현하기

```react
import React, { useState } from "react";

const EventPractice = () => {
  const [username, setUsername] = useState("");
  const [message, setMessage] = useState("");
  const onChangeUsername = (e) => setUsername(e.target.value);
  const onChangeMessage = (e) => setMessage(e.target.value);
  const onClick = () => {
    alert(`${username}: ${message}`);
    setUsername("");
    setMessage("");
  };
  const onKeyPress = (e) => {
    if (e.key === "Enter") {
      onClick();
    }
  };

  return (
    <div>
      <h1>이벤트 연습</h1>
      <input
        type="text"
        name="username"
        placeholder="사용자명"
        value={username}
        onChange={onChangeUsername}
      />
      <input
        type="text"
        name="message"
        placeholder="아무거나 입력해보세요"
        value={message}
        onChange={onChangeMessage}
        onKeyPress={onKeyPress}
      />
      <button onClick={onClick}>확인</button>
    </div>
  );
};

export default EventPractice;

```

```react
import React, { useState } from "react";

const EventPractice = () => {
  // input 태그의 값들이 담겨 있는 form 객체
  const [form, setForm] = useState({
    username: "",
    message: "",
  });
  const { username, message } = form;
  const onChange = (e) => {
    const nextForm = {
      ...form, // 기존의 form 내용을 복사
      [e.target.name]: e.target.value, // 덮어쓰기
    };
    setForm(nextForm);
  };
  const onClick = () => {
    alert(`${username}: ${message}`);
    setForm({
      username: "",
      message: "",
    });
  };
  const onKeyPress = (e) => {
    if (e.key === "Enter") {
      onClick();
    }
  };

  return (
    <div>
      <h1>이벤트 연습</h1>
      <input
        type="text"
        name="username"
        placeholder="사용자명"
        value={username}
        onChange={onChange}
      />
      <input
        type="text"
        name="message"
        placeholder="아무거나 입력해보세요"
        value={message}
        onChange={onChange}
        onKeyPress={onKeyPress}
      />
      <button onClick={onClick}>확인</button>
    </div>
  );
};

export default EventPractice;

```



## 4.4 정리

- 리액트에서의 이벤트는 JS or jQuery와 유사
- 8장의 useReducer 와 커스텀 Hooks 사용하면 더욱 편리 할 것임