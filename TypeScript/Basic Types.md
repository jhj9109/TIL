# 0. Introduction
- 유요한 프로그램은 숫자, 문자열, 구조체, 불리언 값과 같은 간단한 데이터 단위가 요구됨
- TS는 JS와 거의 동일한 데이터 타입을 지원
- 열거 타입을 사용하여 더 편리한 사용이 가능

# 1. Boolean
```typescript
let isDone: boolean = false;
```

# 2. Number
- JS처럼 TS의 모든 숫자는 부동 소수 값
- TS는 16진수, 10진수, ES15의 2진수와 8진수 리터럴까지 지원
```typescript
let decimal: number = 0;
let hexz: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
```

# 3. String
- TS 역시 텍스트 데이터 타입은 `string`으로 표현, `'`나 `"`로 문자열 데이터를 감싸는데 사용
- 템플릿 문자열 사용시 #{ expr } 같은 표현식을 포함 가능
```typescript
let color: string = "blue";
color = 'red';
let fullName: string = `HyeonJun Jang`;
let age: number = 30;
let sentence: string = `Hello, My name in ${fullName}
I'll be ${ age + 1 } years old next year.`
```

# 4. Array
- 배열 타입 표현법 2가지
- 첫번째 : 배열 요소들을 나타내는 타입 뒤에 []
- 두번째 방법 : 제네릭 배열 타입 사용
```typescript
let list1: number[] = [1,2,3];
let list2: Array<number> = [1,2,3];
```

# 5. Tuple
- 요소의 타입과 개수가 고정된 배열을 표현
- 요소들의 타입은 같은 필요 X
```typescript
let x: [string, number];

x = ["hello", 10]; // 성공
x = [10, "hello"]; // 오류

// 정해진 인덱스에 위치한 요소에 접근시 해당 타입이 나타냄
console.log(x[0].substring(1)); // 성공
console.log(x[1].substring(1)); // 오류, 'number'에는 substring X

// 정해진 인덱스 초과 오류
x[3] = "world"; // 오류, '[string, number]' 타입에는 property '3'이 X
console.log(x[5].toString()); // '[string, number]' 타입에는 property '5'이 X
```

# 6. Enum (열거)
- enum은 값의 집합에 더 나은 네이밍 가능
```typescript
enum Color {Red, Green, Blue}
let c: Color = Color.Green;
```
- enum은 0부터 번호를 매기지만, 수동으로 변경 가능
```typescript
enum Color {Red = 1, Green, Blue} // 1부터 시작 1,2,3
enum Color2 {Red = 1, Green = 2, Blue = 4} // 모두 수동 설정 가능
```
- enum의 활용 방안
```typescript
enum Color {Red = 1, Green = 2, Blue = 4}
let colorName: string = Color[2];

console.log(colorNmae); // 'Green'이 출력
```

# 7. Any
- 알지 못하는 타입 표현에 활용 => 타입 검사 없이 컴파일 통과
```typescript
let notSure: any = 4;
notSure = "maybe a string insteed";
notSure = false; // 성공, Boolean임
```
- object는 변수에 할당할 수 있게 하지만 메서드는 임의로 호출 불가
```typescript
let notSure: any = 4;
notSure.ifItExists(); //성공, ifItExists는 런타임엔 존재
notSure.toFixed(); // 성공, toFixed는 존재 (하지만 컴파일러는 검사 X)

let prettySure: Object = 4;
prettySure.toFixed(); // 오류, property 'toFixed'는 'Object'에 존재하지 않음
```
- 타입의 일부만 알때 유용 & 여러 다른 타입이 섞인 배열 구현 가능
```typescript
let list: any[] = [1, true, "free"];

list[1] = 100
```

# 8. Void
- `void` : 어떤 타입도 존재할 수 없음을 나타냄, 반환값이 없는 함수 타입 표현에 활용
- null과 undefined만 할당이 가능하여 void 선언은 유용하진 않음
```typescript
function warnUser(): void {
    console.log("This is my warning message");
}

let unusable: void = undefined;
unusable = null; //  성공, `--strictNullChecks` 을 사용하지 않을때만
```

# 9. Null & Undefined
- 각각 자신의 타입이름 자신의 이름을 사용
- void처럼 그 자체로 유용한 경우 X
```typescript
let u: undefined = undefined;
let n: null = null
```
- null 과 undefined는 `다른 모든 타입의 하위 타입` => 다른 타입에 할당 가능
- 단, `--strictNullChecks` 사용시 `any`와 자신의 타입에만 할당 가능
  - (예외 : void에 undefined 할당 가능)'
- 위의 제약은 일반적인 에러방지에 도움이 됌
-  `--strictNullChecks` 사용시 유니언 타입 활용 `string | null | undefined`
   - 유니언 타입은 상급 주제로, 이후 챕터에서 다루게 될것
   - `--strictNullChecks`은 사용을 권장. 단, 핸드북에서는 사용하지 않는다고 가정 (for 간결함)

# 10. Never
- 절대 발생할 수 없는 타입
- 함수 표현식 or 화살표 함수 표현식에서 항상 오류를 발생시키거나 절대 반환하지 않는 반환 타입으로 활용
- 변수또한 타입 가드에 의해 아무 타입도 얻지 못하면 never 타입을 얻게 된다
- never 타입은 모든 타입에 할당 가능한 하위 타입.
- But 어떤 타입도 never에 할당 불가 & 하위 타입 존재X
```typescript
// never를 반환하는 함수는 함수의 마지막에 도달할 수 없다
function error(message: string): never {
    throw new Error(message);
}

// 반환 타입이 nver로 추론된다.
function fail() {
    return error("Something faled");
}

// nver를 반환하는 함수는 함수의 마지막에 도달할 수 없다.
function infiniteLoop(): never {
    while (true) {

    }
}
```

# 11. Object (객체)
- `object는 원시 타입이 아닌 타입`을 나타냄
  - 원시타입 : number, string, boolean, bigint, symbol, null, undefined
```typescript
declare function create(o: object | null): void;

create({ prop: 0 }); // 성공
create(null); // 성공

create(42); // 성공
create("string"); // 성공
create(false); // 성공
create(undefined); // 성공
```

# 12. Type assertions (타입 단언)
- 타입 단언은 컴파일러에게 "개발자인 날 믿으라구!" 얘기하는 것
- 다른 언어의 타입 변환(형 변환)과 유사하지만, 특별한 검사및 데이터 재구성이 없음
- => 런타임 영향 X, only 컴파일러만 사용
- 첫번째 방법 : `anle-bracket` syntax
```typescript
let someValue: any = "this is a string"

let strLength: number = (<string>someValue).length;
```
- 두번째 방법 : `as`
```typescript
let someValue: any = "this is a string"
let strLength: number = (someValue as string).length
```
- 위 두 방식중, TS를 JSX와 함께 사용시 `as` 스타일만 지원

# @. let
- ES2015에서 소개된 키워드.