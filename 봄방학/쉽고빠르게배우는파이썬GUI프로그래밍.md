# 1일차
> 목표 : 파이썬 GUI 프로그래밍 절차 이해 >>> 창 생성, widget 생성 & 옵션 지정
> 컨텐츠 : tkinter 모듈 / importing , 창 생성, widget 생성 & 옵션지정

## tkinter (티케이 인터)
Tcl (Tool Command Language) / Tk(Tool Kit)
> Unix, Mac os, windows 등에서 GUI응용 프로그램을 개발할 수 있는 도구
**tkinter**
> Python의 표준 GUI 라이브러리
> Python에서 Tcl/Tk 처리하기 위한 GUI 모듈
장점 : 파이썬에 기본 내장, 객체지향 인터페이스, 쉽고 빠르고 간결한 코드

tkinter 활용 개발절차
1. tkinter 모듈 import
2. 메인 윈도우 생성
3. 메인 윈도우에 위젯 (버튼, 메듀) 추가
4. 이벤트 핸들링 등 원하는 코드 작성

윈도우 생성 / 제목 바꾸기 & 위젯 추가 및 실행
```python
import tkinter
win = tkinter.Tk()
# .Tk() : 윈도우 인스터스 생성
win.title('윈도우 생성하기')

lbl = tkinter.Label(win, text = "안녕 파이썬~")
lbl.pack()
lbl2 = tkinter.Label(win, text="hello world~", bg='red', fg='white')
lbl2.pack(fill='x')
win.mainloop()
```
`.Tk()` : 윈도우 인스턴스 생성
`.title('이름')` : 윈도우 타이틀 변환
`.laber(윈도우 인스턴스, text = '출력 텍스트')` : 위젯 추가
`.pack()` : 위치시킨다 == 패킹
`bg` : background 색깔
`fg` : 글자 색깔

위젯이란
- Label, Button, Check Button 등 GUI의 핵심 요소
- 사용자에게 내용 안내, 선택을  받아들이는 등 interactive한 처리 가능케함

위젯이름 : 목적
Label : 사용자에게 텍스트, 이미지 제시
Message : 텍스트를 표시 (Label과 유사하나, 자동래핑(줄바꿈)이 됨)
Button : 버튼의 역할 (특정명령의 실행)
CheckButton : 체크박스 (선택을 받아 들일때)
RadioButton : 옵션 버튼 (여러 항목 제시, 하나의 선택 받는 버튼)
Entry : 한 줄 텍스트 입력 받을때
Text : 여러 줄 텍스트를 입력 및 편집하는 위젯, Rich Text 기능 제공
ListBox : 리스트박스(여러 텍스트 항목을 줄 단위로 표시하고 선택을 유도)
Scale : 특정범위 내에서 사용자의 가시적 조작을 통해 값을 선택 (ex : 0~100)
Scrollbar : 스크롤 바 (다른 위젯과 연동 가능)
Spinbox : 사용자에게 값을 제시, 업다운 화살표를 통해 선택토록 함
Menu : 메뉴 (드롭다운 메뉴 제공)
Menubutton : 버튼식 메뉴
Toplevel : 최상위 창
Frame : 다른 위젯들을 그룹화하는 판넬의 역할
Canvas : 그래프와 점 등으로 그림을 그릴 수 있다.

1. Label
`w = Label(master, option, ...)`
> 텍스트나 이미지를 표시하는 위젯
> 필요할때 프로그램상에서 내용 변경 가능
> 사용자 입력 불가, 입력은 Entry or Text위젯 활용

widget의 생성
`w = widget_classname (parent, option, ...)`
ex : lbl = Label(win, option, ...)
lbl-변수명(객체인스턴스)
Label 레이블 클래스명
win 소속지정 (상위 윈도우, 위젯)
option 생성 옵션 (크기, 색 등등)

Label 옵션
옵션명 : 의미 : 기본값 : 속성
텍스트 관련
text : 레이블에 표시할 문자열 : - : -
textvariable : 레이블의 문자열 저장변수 : - : -
anchro : 할당공간 내에서 표시위치 : center - n, ne, e, se, s, sw, w, nw, center
justify : 문자열 정렬방식 : center : center, right, left
wraplenth : 자동 줄내림 설정 너비 : 0 : 상수
모양 / 색 관련
width,height : 너비 , 높이 : 0 : 상수
relief : 테두리 모양 : falt : flat, groove, raised, ridge, solid , sunken
borderwidth(bd) : 테두리 두께 : 2 : 상수
borderground(bg) : 배경 색상 : SystemButtonFace : color
foreground(fg) : 문자열 색상 : SystemButtonText : color
padx : 테두리와 내용의 가로 여백 (내부채움) : 1 : 상수
pady : 테두리와 내용의 세로 여백 : 1 : 상수
상태 관련
state : 상태 : normal : normal, active(마우스 위에), disabled(먹통)
activebackground : active상태일때 배경 색상 : SystemButtonFace : color
activeforeground : active상태일때 문자열 색상 : SystemButtonText : color
disabledforeground : active상태일때 배경 색상 : SystemDisabledTextFace : color
포커스 & 하이라이트 관련
takefocus : 포커스 여부 : False : True
highlightcolor : 선택되었을때 보더 색상 : SystemWindowFrame : color
highlightbackground : 선택되지않았을때 보더 색상 : SystemButtonFace : color
highlightthickness : 선택되었을때 보더 두께 : 0 : color

```python
import tkinter
win = tkinter.Tk()
ent1 = tkinter.Entrt(win,
                        relief = 'ridge',
                        borderwidth = 3,
                        highlightcolor = 'red',
                        highlightthickness = 3,
                        highlightbackground = 'yellow',
                        takefocus = True )
end1.pack()

ent2 = tkinter.Entry(win,
                        relief = 'ridge',
                        highlightcolor = 'red',
                        highlightthickness = 'yellow',
                        takefocus = True)
ent2.pack()
win.mainloop()
```

생성되어 있는 위젯의 옵션 변경 >>> config() 메서드 , key로 옵션접근
```python
import tkinter

win = tkinter.Label(win, text = 'Hello World!')
hello.pack()
hello.config(text='안녕파이썬')
hello['text'] ='안녕파이썬'
```
레이블.config(text = :" 바꿀 텍스트") #configure 써도 똑같음
레이블['text'] = '바꿀 텍스트'