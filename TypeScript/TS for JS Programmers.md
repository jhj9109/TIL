# 서론
- TS는 JS기능을 제공하며 자체 레이어인 `Type System`을 추가한다.
- JS는 원시타입 (string, number, object, undefiend) 등을 갖지만, 일관되게 할당되었는지 미리 확인 X
- TS는 원시타입이 일관되게 할당되었는지 미리 확인해준다.
- TS의 Type Checker : 개발자의 의도와 JS가 실제로 수행하는 일 사이의 불일치를 강조

Types System 5분 개요!
# Types by Inference (타입 추론)

- 자동으로 타입 제공하는 경우임
- 변수 생성과 동시에 특정 값을 할당하는 경우 => TS는 그 값을 해당 변수의 타입으로 활용

# Defining Types (타입 정의)
- 동적 프로그래밍 사용 => 자동으로 타입 제공이 힘듬
- TS는 JS언어의 확장을 지원, 타입을 명시토록 돕는다.
```
// 타입 추론
const inferenceUser = { name: "jhj", id:0 }

// 타입 정의
interface User { name: string, id:number }

// 변수뒤에 TypeName 구문을 사용해 interface를 따르고 있음을 알림
const user: User = { name: "jhj", id:0 }
```
- JS처럼 TS또한 클래스와 객체 지향 프로그래밍 지원 => interface도 class로 선언 가능
```
interface User {
    name: string;
    id: number,
}

class UserAccount {
    name: string;
    id: number;

    constructor(name: string, id: number) {
        this.name = name;
        this.id = id;
    }
}

const user: User = new UserAcoount("jhj", 1);
```

- interface는 함수에서 `매개변수`와 `리턴값` 명시하는데도 사용

```typescript
interface User {
	name: string;
    id: number;
}

function getAdminUser(): User {
    //...
}

function deleteUser(user: User) {
    //...
}
```

- 기존 JS의 원시 타입은 모두 인터페이스 사용 가능
  - boolean, bigint, null, number, string, symbol, object, undefined

- TS는 여기에 몇가지 추가
  - `any`  : 무엇이든 허용
  - `unknown`  : 이 타입을 사용하는 사람이 타입이 무엇인지 선언했는가를 확인
  - `never` : 이 타입은 발생 될 수 없음
  - `void` : undefined 리턴 or 리턴 X
-  Type을 구축하기 위한 2가지 Syntax : interface, type



# Composing Types (타입 구성)

- 여러 Types을 이용해 새 type을 작성하기 위한 Union, Generic



## 1. Unions

- Type이 여러 타입 중 하나일 수 있음을 선언하는 방식
- `type MyBool = true | false`
  - 참고 : MyBool은 boolean으로 분류 => 구조적 타입 시스템의 property
- string || number 리터럴집합을 설명시 사용
  - `type WindowStates = "open" | "closed" | "minimized";`
  - `type LockStaets = "locked" | "unlocked"`
  - `type OddNumbersUnderTen = 1 | 3 | 5 | 7 | 9`

- 다양한 Type 처리하는 방법을 제공

  ```typescript
  function getLength(obj: string | string[]) {
  	return obj.length
  }
  ```

- Type 검사 : `typeof 변수 === "비교할 타입"`

### 2. Generics

- 타입에 변수를 제공하는 방법

- ex : 배열 => 제너릭이 없는 배열은 어떤 것이든 포함 가능, 제너릭이 있는 배열은 배열 안의 값을 설명 가능

  ```typescript
  type StringArray = Array<string>;
  type NumberArray = Array<number>;
  type ObjectWithNameArray = Array<{ name: string }>
  ```

- 제너릭을 사용하는 고유 타입 선언

  ```typescript
  interface Backpack<type> {
      add: (obj: Type) => void;
      get: () => Type;
  }
  
  // 이 줄은 TypeScript에 "backpack"이라는 상수가 있음을 알리는 지름길이며
  // const backpack: Backpack<string>이 어디서 왔는지 걱정할 필요 X
  
  // 위에서 BackPack의 변수 부분으로 선언하여 object는 string입니다.
  const object = backpack.get();
  
  // backPack 변수가 string이므로, add 함수에 number를 전달할 수 없습니다.
  backpack.add(23);
  ```

  

## 3. Structural Type System

- TS 핵심원칙 중 하나 : 형태에 집중 => dyck typing (or 구조적 타이핑)

- 구조적 타입 시스템 => 구 객체가 같은 형태 => 같은 것

  ```typescript
  interface Point{
      x: number;
      y: number;
  }
  
  function printPoint(p: Point) {
      console.log(`${p.x}, ${p.y}`);
  }
  
  // "12, 26"를 출력
  const point = { x: 12, y: 26}
  printPoint(point)
  ```

  - `point` 변수는 `Point` 타입으로 선언된 적이 없지만, TS는 Type 검사에서 `point` 와 `Point` 형태를 비교. 같으면 통과

  - 형태 일치에는 일치시킬 객체의 필드의 하위 집합만 필요

    ```typescript
    interface Point {
      x: number;
      y: number;
    }
    
    function printPoint(p: Point) {
      console.log(`${p.x}, ${p.y}`);
    }
    // ---cut---
    const point3 = { x: 12, y: 26, z: 89 };
    printPoint(point3); // prints "12, 26"
    
    const rect = { x: 33, y: 3, width: 30, height: 80 };
    printPoint(rect); // prints "33, 3"
    
    const color = { hex: "#187ABF" };
    
    printPoint(color);
    ```

    

- 구조적으로 클래스와 객체가 형태를 따르는 방법에는 차이 X

  ```typescript
  interface Point {
    x: number;
    y: number;
  }
  
  function printPoint(p: Point) {
    console.log(`${p.x}, ${p.y}`);
  }
  // ---cut---
  class VirtualPoint {
    x: number;
    y: number;
  
    constructor(x: number, y: number) {
      this.x = x;
      this.y = y;
    }
  }
  
  const newVPoint = new VirtualPoint(13, 56);
  printPoint(newVPoint); // prints "13, 56"
  ```

  - 객체 또는 클래스에 필요한 모든 속성이 존재한다면 TS는 구현 세부 정보에 관계없이 일치하게 봄