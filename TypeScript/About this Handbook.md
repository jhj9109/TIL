# 서론
- JS는 cross-platform Language
- JS의 시작은 Web Page의 상호작용을 위한 작은 Scripting Language
- 현재는 FE, BE Application 전반적인 영역에서 사용 가능한 Language로 성장
- JS의 언어 능력 중 다른 코드 단위 간의 관계를 표현하는 능력은 발전하지 못함
- JS 특이한 Runtime Semantics & 언어와 프로그램 복잡성 불일치 => 문제
- 가장 흔한 error는 Type Error
- TS의 목표는 JS 프로그램의 `정적` `타입 검사`자
  - 정적 : 코드가 실행되기 전에 실행
  - 타입 검사 : 프로그램 타입이 정확한지 확인

# 핸드북 소개
## 핸드북 구성
핸드북은 2가지 영역으로 구분
1. 핸드북
   - 각 장 or 페이지는 주어진 개념에 대한 설명 제공
   - 모든 특징과 동작에 대한 종합 가이드
   - 실습 완료한 독자는 아래를 수행할 수 있을것이다.
     - 일반적인 TS Syntax & Pattern 읽고 이해
     - 중요한 컴파일러 옵션의 효과
     - 대부분의 경우에서의 Type System 동작 올바른 예측
     - 간단한 함수 or 객체 or 클래스에 대한 .d.ts 선언 작성
   - 명확성과 간결성을 위해, 모든 엣지 케이스를 탐구하진 않음 
2. 핸드북 레퍼런스
   - TS의 특정 부분의 작동에 대한 풍부한 이해를 제공
   - 각 세션은 단일 개념에 대한 깊은 설명 제공
## 잠재적인 목표 (Non-Goals)
- 간결한 문서 지향을 위해, 특정 주제는 다루지 않은 것들이 존재
- 특히 함수, 클래스, 클로저 같은 JS 핵심 개념은 전부 소개하지 않은 대신 배경 자료 링크 제공
- 핸드북은 언어 명세 대체 X
- 필요한 경우가 아니면 TS의 다른 도구와의 상호작용을 다루지 않음.
- webpack, rollup, parcel, react, babel, closure, lerna, rush, bazel, preact, vue, angular, svelte, jquery, yarn, npm으로 TS를 구성하는 방법은 다른 Website에서 서치