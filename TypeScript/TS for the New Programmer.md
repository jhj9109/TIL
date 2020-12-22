# JS의 짧은 역사
- 브라우저를 위한 스크립트 언어 => 짧은 코드용
- 실행 엔진(동적 컴파일) 최적화 => API 추가 => 확장

# JS로 인해 발생되는 문제들
- `==` operator : 인수를 강제 변환 => 예상치 못한 결과 도출
    - `"" == 0` : true
    - `1 < x < 3` : (어떤 x든) true
- 존재하지 않는 property 접근 허용
    - ```
        const obj = { a:1, b:2 };
        const area = obj.a * obj*b; // 결과 : NaN
        ```
- JS는 위와 같은 상황에서 오류를 발생시키지 않아, 관리가 힘들다.

# TypeScipt : A Static Type Checker
- TS는 정적 타입 검사자
- `정적 검사` : 프로그램을 실행시키지 않고 코드의 오류를 검출하는 것

## 1. A Typed Superset of JS
### Syntax
- TS는 JS의 Syntax이 허용되는 JS의 상위 집합 언어.
    - Syntax (구문) : 프로그램을 만들기 위해 코드를 작성하는 방법 (문법이랄까?)
    - JS코드를 TS 파일에 넣어도 잘 작동한다.

### Types
- TS는 다른 종류의 값들을 사용할 수 있는 방법이 추가된 `Type이 있는` Superset이다.
- 예시 : `console.log( 4 / [] ) `
    - JS : syntactically-legal => `NaN` 출력
    - TS : 오류 발생

### Runtime Behavior
- TS는 JS의 런타임 특성을 갖는 프로그래밍 언어
- 즉 타입 오류가 있는 코드여도, 동일한 코드라면 JS파일, TS파일 모두에서 같은 동작
- 두 언어간의 쉬운 전환을 위한 TS의 약속

### Erased Types
- TS는 코드 검사를 마친후, 타입을 삭제(컴파일 행위)하여 "컴파일된 코드"를 생성
- 이것은 TS가 추론한 타입에 따라 프로그램의 특성을 변화시키지 않기위함
- 컴파일 도중 타입 오류 표출은 가능, But 프로그램 실행시 작동되는 방식에 영향은 X

### 추가 런타임 라이브러리 Nob!
- TS는 JS와 같은 표준 라이브러리 (or 외부 라이브러리)를 사용하므로, TS관련 추가 공부가 불필요하다.

## 2. Learning JS & TS
- TS는 `컴파일-타임 타입 검사자가 있는 JS의 런타임`이다!