# 1일차

> 목표 : 파이썬 GUI 프로그래밍 절차 이해 >>> 창 생성, widget 생성 & 옵션 지정
> 컨텐츠 : tkinter 모듈 / importing , 창 생성, widget 생성 & 옵션지정

## tkinter (티케이 인터)

Tcl (Tool Command Language) / Tk(Tool Kit)

> Unix, Mac os, windows 등에서 GUI응용 프로그램을 개발할 수 있는 도구
> **tkinter**
> Python의 표준 GUI 라이브러리
> Python에서 Tcl/Tk 처리하기 위한 GUI 모듈
> 장점 : 파이썬에 기본 내장, 객체지향 인터페이스, 쉽고 빠르고 간결한 코드

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
`.Label(윈도우 인스턴스, text = '출력 텍스트')` : 위젯 추가
`.pack()` : 위치시킨다 == 패킹
`bg` : background 색깔
`fg` : 글자 색깔

**위젯이란**

- **Label, Button, Check Button 등 GUI의 핵심 요소**
- 사용자에게 내용 안내, 선택을  받아들이는 등 **interactive한 처리 가능케함**

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

|                         옵션명                          |                 의미                 |         기본값         |                    속성                     |
| :-----------------------------------------------------: | :----------------------------------: | :--------------------: | :-----------------------------------------: |
|                       텍스트 관련                       |                                      |                        |                                             |
|                          text                           |        레이블에 표시할 문자열        |           -            |                      -                      |
|                      textvariable                       |       레이블의 문자열 저장변수       |                        |                                             |
|                         anchor                          |       할당공간 내에서 표시위치       |         center         |     n, ne, e, se, s, sw, w, nw, center      |
|                         justify                         |           문자열 정렬방식            |         center         |             center, right, left             |
|                        wraplenth                        |        자동 줄내림 설정 너비         |           0            |                    상수                     |
|                     모양 / 색 관련                      |                                      |                        |                                             |
|                      width,height                       |              너비, 높이              |           0            |                    상수                     |
|                         relief                          |              테두리모양              |          flat          | flat, groove, raised, ridge, solid , sunken |
|                     borderwidth(bd)                     |             테두리 두께              |           2            |                    상수                     |
|                    borderground(bg)                     |              배경 색상               |    SystemButtonFace    |                    color                    |
|                     foreground(fg)                      |             문자열 색상              |    SystemButtonText    |                    color                    |
|                          padx                           | 테두리와 내용의 가로 여백 (내부채움) |           1            |                    상수                     |
|                          pady                           |      테두리와 내용의 세로 여백       |           1            |                    상수                     |
|                        상태 관련                        |                                      |                        |                                             |
|                          state                          |                 상태                 |                        | normal, active(마우스 위에), disabled(먹통) |
|                    activebackground                     |       active상태일때 배경 색상       |    SystemButtonFace    |                    color                    |
|                    activeforeground                     |      active상태일때 문자열 색상      |    SystemButtonText    |                    color                    |
|                   disabledforeground                    |      disabled상태일때 배경 색상      | SystemDisabledTextFace |                    color                    |
|                포커스 & 하이라이트 관련                 |                                      |                        |                                             |
|                        takefocus                        |             포커스 여부              |         False          |                    True                     |
|                     highlightcolor                      |        선택되었을때 보더 색상        |   SystemWindowFrame    |                    color                    |
| : 선택되지않았을때 보더 색상 : SystemButtonFace : color |      선택되지않았을때 보더 색상      |    SystemButtonFace    |                    color                    |
|                   highlightthickness                    |        선택되었을때 보더 두께        |           0            |                    상수                     |



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

# 2일차 widget의 배치 & 꾸미기

> 목표 : tkinter geometry 이해, widget을 창에 최적 배치 & 세부 옵션 구분 지정
>
> 콘텐츠 : geometry manager, pack & grid, place, widget배치의 세부 옵션

위젯의 배치

### 1. pack()

|     옵션      |                 의미                 | 기본값 |                 값                 |
| :-----------: | :----------------------------------: | :----: | :--------------------------------: |
|     side      |         해당 구역 할당/배치          |  top   |      top, bottom, left, right      |
|    anchor     |         할당공간 내 위치지정         | center | n, ne, e, se, s, sw, w, nw, center |
|     fill      |       할당공간 내 크기 채우기        |  none  |          none, x, y, both          |
|    expand     |      비할당 공간까지 위젯 확장       | False  |               T / F                |
| ipadx / ipady |   위젯에 대한 x, y 방향 내부 패딩    |   0    |                상수                |
|  padx / pady  | 위젯에 대한 x,y 방향 외부 패딩(여백) |   0    |                상수                |

```python
import tkinter

win = tkinter.Tk()
win.geometry("300x300")

hello = tkinter.Label(win, text = 'Hello World!', relief = 'ridge')
hello.pack(side = 'left')
```

윈도우공간 > 할당공간 > 사용공간 & 미사용공간 

### 2. grid()

- grid은 모든 frame dmf 행렬격자구조 테이블로 처리
- cell은 행과 열의 교차점
- 열의 너비 -- : 해당 열에서 가장 넓은 셀의 너비
- 행의 높이 -- : 해당 행에서 가장 높은 셀의 높이
- 여러 셀을 하나의 영역으로 spnning 할 수 있다
- 지오메트리에 등록해야 화면에 나타남
- 위젯은 grid에서 일반적으로 하나의 셀만 점유

옵션

- row, column : 옵션으로 표시될 행과 열을 지정
- columaspan, rowspan : 옵션 지정 시 여러 셀 병합
- padx, pady : 위젯의 외부에 빈 공간으로 패딩
- ipadx, ipady : 위젯 자체의 크기 확장으로 패딩
- sticky : 여분공간에서 위젯의 배치를 어찌할지 결정 W, E, N, S 등



```python
from tkinter import *
win = Tk()
ent = Entry(win).grid(row = 0, column = 0, columnspan = 3)

f = "굴림", 10
btn1 = Button(win, font = f, text = '1-0', width = 4, height = 2)
btn1.grid(row = 1, column = 0)
btn2 = Button(win, font = f, text = '1-1', width = 4, height = 2)
btn2.grid(row = 1, column = 1)
btn3 = Button(win, font = f, text = '1-2', width = 4, height = 2)
btn3.grid(row = 1, column = 2)
```

### place

> 위젯의 x,y 좌표값을 지정하므로 좀더 정밀한 배치 가능
>
> 픽셀 단위의 수평, 수직 오프셋값

`widget.place(x = 20, y = 20)`

```python
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry('330x250')

b1 = ttk.Button(win, text='불러오기')
b1.place(x = 10, y = 10, width = 100)

b2 = ttk.Button(win, text='처리하기')
b2.place(x = 115, y = 10, width = 100)

b3 = ttk.Button(win, text='저장하기')
b3.place(x = 220, y = 10, width = 100)

tx = Text(win)
tx.place(x = 10, y = 45, width=310)

win.mainloop()
```

## 창의 위치와 크기 지정

> geometry('geometry string')메서드

`win.geometry('WxH + X + Y')`

W : 넓이(픽셀)

H : 높이

X : 화면좌측 모서리로부터의 X좌표

Y : 화면좌측 모서리로부터의 Y좌표

## 위젯의 3D효과 (relief)지정

sunken : 움푹 파인 것

ridge : 테두리만 튀어나온 것

groove : 테두리 경계

raised : 높이 솟은 것

## font 지정

방법1 : 위젯 생성시 순서에 맞추어 font string 지정

family size weight slant underline overstrike

family : 폰트 이름

size : 사이즈

weight : 두께 (bold, normal)

slant : 기울림 (italic, roman)

underline : 언더라인

overstrike : 오버라인

방법2 : tkinter font 모듈 활용

```python
from tkinter import *
import tkinter.font as ft
win = Tk()
f = ft.Font(family = "HY헤드라인M",
          	size = 16,
           weight = 'bold',
           slant = 'italic',
           underline = True)
lbl = Label(win, text = "안녕 파이썬", font = f)
lbl.pack()

win.mainloop()
```

# 3일차 다이얼로그와 메뉴의 표현

> 목표 : 버튼 배치, 실행 명령 작성 가능, file처리 다이얼로그 생성 및 처리, color처리 다이얼로그를 생성 및 처리
> 내용 : 버튼 배치, 커맨드 옵션과 처리기, file dialog, color dialog

## Message

> Label과 유사, 여러 줄에 텍스트 디스플레이 가능

```python
from tkinter import *
win = Tk()

lbl = Message(win, text = "텍스트내용 \
    계속되는 텍스트 내용")
lbl['font'] = '굴림체 15 bold'

lbl.pack()
win.mainloop()
```

## Frame

> 프레임은 다른 위젯을 그룹화하여 배치하는 일종의 컨테이너 역할 (기존 win)

- `w = Frame (master, option, ....)`

## LabelFrame

> Label을 가진 Frame

- `w = LabelFrame (master, option, ....)`
- 옵션 : text, labelanchor

```python
from tkinter import *
win = TK()
lframe = LabelFrame(win, text = '이름', padx = 5, pady = 5)
lframe.pack(padx = 10, pady = 10)

e = Entry(lframe)
e.pack
```

## Button

- `w = Button (master, option=value, ...)`
- 응용 프로그램에 버튼을 표시하는데 사용 (특정 명령수행)
- 텍스트나 이미지 표시 가능
- 버튼에 함수 연결 가능 -> 클릭 시 자동 호출

Button 메서드

- invoke() 메서드 : 콜백호출 (코드상에서)
- flash() 메서드 : 깜빡(기본색상과 activebackground)

```python
from tkinter import *
from tkinter import messagebox as m

def btn_click():
    lbl['text'] = ' have a good day~~'
    m.showinfo('인사완료', '인사를 마쳤습니다.')

wim = Tk()
win.geometry('300x60')
lbl = Label(win, text = '안녕하세요 파이썬 ~", head = "HY헤드라인M 20")
lbl.pack()

btn = Button(win, text = "눌러주세요", command = btn_click, bg = 'red', fg = 'white')
btn.pack(fill = 'x')
```

## 메시지박스 모듈

> 메시지 박스를 보여주거나 사용자 응답을 요구하는데 사용하는 모듈
> 모듈을 통해 다이얼로그 박스 관련 다양한 함수에 접근 할 수 있음

1. 모듈 import
2. 모듈을 통해 함수 call
3. 사용자 응답에 따른 처리

```python
from tkinter import *
from tkinter import messagebox as m
win = Tk()
win.title("메시지박스 테스트")
win.geometry('350x200')
def clicked():
    m.showinfo('저장확인', '저장되었습니다')
    m.showwarnning('용량부족', '저장공간이 부족합니다')
    m.showerror('에러발생', '에러가 발생했습니다. 종료합니다.')
    res = m.askquestion('저장확인', '정말 덮어쓰시겠습니까?') # yes / no
    res = m.askyesno('종료확인', '정말 종료합니까?') # T/F
    res = m.askyesnocancel('Message title', 'Message content')# T/F/None
    res = m.askokcancel('Message title', 'Message content')# T/F
    res = m.askretrycancel('Message title', 'Message content')# T/F
btn = Button(win, text = 'Click here', command=clicked)
btn.grid(column = 0, row = 0)
win.mainloop()
```

## 파일 다이얼로그 모듈

```python
from tkinter import filedialog
#filetypes 예
f =(("설명할 텍스트", "*.tplate"),#템플릿
            ("설명할 텍스트2", "*.html;*.htm"),#HTML
            ("설명할 텍스트3", "*.txt"), #텍스트
            ("설명할 텍스트4", "*.*")) #모든파일
filename = filedialog.askopenfilename( filetypes = f )
#filename = filedialog.asksavesfilename( filetypes )
```

## 색상 다이얼로그 모듈

```python
from tkinter import colorchooser
c = colorchooser.askcolor()
```

## 다이얼로그 예제

```python
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser

win = tk.Tk()

def open_click():
    s = (("텍스트파일", "*.txt"),)
    fname = filedialog.askopenfilename( filetypes = s)
    if fname != "":
        f = open(fname, 'r')
        data = f.read()
        tx.insert('insert', data)
def color_click():
    color = colorchooser.askcolor()
    tx['bg'] = color[1]
tx = tx.Text(win, width = 80, height = 20)
tx.pack(side = 'top', fill = 'both' expand = True)
btn = tk.Button(win, text = '파일불러오기', command = open_click)
btn.pack()

btn2 = tk.Button(win, text = '바탕색 변경', command = color_click)
btn2.pack()
win.mainloop()
```

## Menu

> 드롭다운식 메뉴를 제공
> Menubutton의 하위개념 - 상위를 눌렀을때 나타난다.
> 옵션 : tearoff 뜯어내기 T/F, tearoffcommand 알림받기, command 메뉴 선택시 실시할 함수 지정

### 메뉴 타입

- cascade : 서브메뉴가 있는 메뉴 (보통메뉴)
- command : 일반 메뉴 (단독)
- Checkbutton : 체크식 메뉴
- Radiobutton : 라디오버튼식 메뉴
- separator : 분리바

### 생성 및 삭제 메서드

- .add(kin, coption, ...)
- .add_cascade, .add_command, .add_checkbutton, .add_radiobutton,
- .delete(index)
- .entryconfig(index, state)

### 메인메뉴 넣기

1. 메뉴 객체 생성
2. 생성된 메뉴 객체에 메뉴 추가
3. 창에 등록

```python
from tkinter import *
win = Tk()
mbar = Menu(win)
mbar.add_cascade(label="파일")
mbar.add_cascade(label="편집")
mbar.add_cascade(label="도움말")
win['menu'] = mbar # win.config(menu = mbar) 동일
win.mainloop()
```

### 서브메뉴 넣기

1. 메뉴 객체 생성
2. 생성된 메뉴객체에 메뉴 추가
3. 상위메뉴에 등록

```python
from tkinter import *
win = Tk()
def menu_click():#개별 특수 동작 미구현
    print("메뉴를 선택했습니다.")
mbar = Menu(win)
fmenu = Menu(mbar, tearoff = False)
fmenu.add_command(label="Open", command=menu_click)
fmenu.add_command(label="Save", command=menu_click)
fmenu.add_separator()
fmenu.add_command(label="Exit", command=menu_click)

mbar.add_cascade(label="파일", menu=fmenu)

win['menu'] = mbar # win.config(menu = mbar) 동일
win.bind_all('<Control s>',menu_click)
win.mainloop()
```

# 4일차 제어변수 활용하기

> 목표 : control variable과 widget의 내부 연동 및 동작원리 이해, 활용
> 내용 : control variable 개요, type, 활용방법(데이터 getting & setting)

## 제어변수 활용하기

### 제어변수(1)

#### 1. 개요

##### 제어변수란 무엇잇가?

- 위젯과 연결, 값을 반영하는 객체
- 체크 버튼 : On/Off
- 라디오 버튼 : 하나의 변수 공유하여 서로간 토글
- 엔트리 : 출력 문자열
- 버튼 : 표시되는 문자열

##### 제어변수 type

- IntVar()
- StringVar()
- BooleanVar()
- DoubleVar()

##### 위젯값 넣기 빼기

- .set(data)
- .get()

#### 2. Menubutton (master, option, ....)

>  w = Menubutton (master, option, ...)

```python
from tkinter import *
def selected():
    k = v.get()
    
    if k == 1:
        print('복사 선택')
    elif k == 2:
        print('붙여넣기 선택')
    elif k == 3:
        print('지우기 선택')
        
win = Tk()
mb = Menubutton(win, text ='편집', relief = RAISED)
mb.grid()
smenu = Menu(mb)
mb['menu'] = smenu
v = IntVar()
smenu.add_radiobutton(label ='복사', variable = v, value = 1, command = selected)
smenu.add_radiobutton(label = '붙여넣기', variable = v, value = 2, command = selected)
smenu.add_radiobutton(label = '지우기', variable = v, value = 3, command = selected)
#selected >>> 선택된 상태로 유지
win.mainloop()
```

#### 3. check버튼

>  w = Check (master, ....)

- 사용자 선택사항을 체크하는 위젯

##### 옵션

- indicatoron : 1 - 일반동작, 0 - 푸시버튼식
- textvariable : 표시되는 문자열 관리 제어변수
- variable : 선택, 비선택 관리 제어변수(onvalue, offvalue 연관)
- onvalue, offvalue : 원래 1, 0 이지만 다른 값 지정시
- command : 체크버튼 상태 변경 시 함수호출

##### 메서드

- deselect() : off상태로
- select() : on 상태로
- invoke() : 누른 효과(콜백) toggle() 토글

##### 예제 (제어변수 활용)

```python
from tkinter import *
def inspect_check():
    print('숙박여부', var1.get())
    print('조식여부', var2.get())
    print('가이드 투어여부', var3.get())
win = Tk()
win.geometry('200x150')
fra = LabelFrame(win, text = '여행상품선택', labelanchor = 'nw', font = '굴림 10 bold')
fra.pack(fill = 'both', padx = 20, ipady = 10)
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
chk1 = Checkbutton(fra, text = '숙박', variable = var1, command = inspect_check)
chk1.pack()
chk2 = Checkbutton(fra, text = '조식', variable = var2, command = inspect_check)
chk2.pack()
chk3 = Checkbutton(fra, text = '투어', variable = var3, command = inspect_check)
chk3.pack()
btn = Button(fra, text = '선택완료', command = inspect_check)
btn.pack()
mainloop()
```

#### 4. Scale

>  w = Scale(master, ....)

- 특정 범위내 가시적 조작을 통해 값 조절

##### option

- from_, to : 값의 범위 지정
- resolution : 간극의 값
- tickinterval : 표시 간격
- jump : 0(마우스 끌을 때마다 콜백), 1(끌다가 놓을때 콜백)
- orient : HORIZONTAL, VERTICAL
- variable : 제어변수

##### 예제

```python
from tkinter import *
win = Tk()
win.geometry('300x200')
v = IntVar()

def value_change(val):
    print('스케일 코멘트', val)

s2 = Scale(win, from_ = 10, to = 100, orient = HORIZONTAL, command = value_change, tickinterval = 10, variable = v)
s2.pack(fill = X)

def select_click():
    print(v.get())
btn = Button(win, text = '선택', command = select_click())
btn.pack()
win.mainloop()
```

```python
from tkinter import *
def font_control(ev):
    label.config(font = "HY헤드라인M %d bold"v.get())

win = Tk()
win.geometry('350x150')
v = IntVar()

label = Label(win, text = '안녕 파이썬~')
label.pack(fill = Y, expand = 1)

sc = Scale(win, from_ = 10, to = 100, orient = HORIZONTAL,
           command = font_control, tickinterval = 10, variable = v)
v.set(14)
sc.pack(fill = X, expand = 1)

def select_click():
    print(v.get())
qbtn = Button(win, text = '끝내기', command = win.quit, font = '굴림 10 bold')
qbtn.pack()
mainloop()
```

#### 5. ttk.Combobox

>  w = ttk.Combobox(master, ....)

- 엔트리 위젯과 드롭다운 메뉴의 콤비네이션 위젯
- 화살표를 눌러 펼쳐진 값을 선택하거나 직접 값을 입력 가능

##### ttk

- ttk는 themed tk widget으로 색상 들 비주얼의 개선

- 매킨토시 GUI수준으로 보임

- tk와 ttk 동시 사용시 import 방식

  ```python
  import tkinter as tk
  from fkinter as ttk
  b1 = tk.Button(...)
  b2 = tkk.Button(...)
  ```

  

##### 옵션

- exportselection : 엔트리에서 텍스트 선택 시 클립보드 자동반출 막을시 0
- height : 드롭다운 시 펼쳐지는 리스트 개수 지정(기본20)
- postcommand : 사용자가 화살표 클릭 시 호출되는 함수
- textavriable : 엔트리 영역에 나타나는 텍스트 제어변수
- **validate : 유효성 검사요청**
- **validatecommand : 유효성 검사 함수 지정**
- values : 드롭다운 리스트에 펼쳐질 값들
- xscrollcommand : 위젯과 연동된 수평 스크롤바가 있는 경우 스크롤바의 set 메소드로 이것 설정

#### 6. Entry

> w = Entry(master, ...)

##### 옵션

- 단일 줄 문자열 입력 받는 위젯 >>> 사용자가 수정할 수 없는 텍스트 줄을 레이블 위젯 사용
- exportselection : 0으로 하면 선택문지열 클립보드 전송을 방지
- insertbackground : 검정삽입커서를 다른 색으로
- insetwidth : 삽입커서 두께
- readonlybackground : 위젯의 state 옵션이 'readonly'시 배경색
- **show : 입력시 보여질 암호문자 (예 : *)**
- **validate : 유효값 입증 옵션**

##### 메서드

- .insert(index, string) : 
- .delete(start, end)
- .get() : 문자값 가져오기
- .icursor(index) : 키보드 커서 설정
- .select_adjust(index) : 지정된 위치까지 선택
- .select_range(start, end)
- .select_to(index) : 커서부터
- .select_from(index) : 커서까지
- .select_clear() : 선택해제

```python
from tkinter import *
from tkinter import messagebox

win = Tk()
v = StringVar()
def ok_click():
    na = v.get()
    lbl2.configure(text = "당신의 이름은" + na +"입니다.")
    messagebox.showinfo("이름", na)
    
lbl = Label(win, text = "이름 : ")
lbl.grid(row = 0, column = 0)
txt = Entry(win, bg = "yellow", textvariable = v)
txt.grid(row = 0,  column = 1)

btn = Button(win, text = "완료", command = ok_click)
btn.grid(row = 0, column = 2)

lbl2 = Label(win, text = "당신의 이름은 : ")
lbl2.grid(row = 2, column = 0, columnspan = 2, sticky = W)
win.mainloop()

*----- txt.focus()
```

#### 7. Radiobutton

> w = Radiobutton(master, ....)

- 라디오 버튼에 하나의 변수를 연결하여 여러 선택항목 제시, 하나의 선택 받는 버튼 구현
- frame, pannel등은 라디오 그룹 형성시 매우 중요

```python
from tkinter import *
def change():
    print ('Station = ', charge[var.get()])
win = Tk()
stations = '대구', '부산', '광주', '여수'
charge =   [1000, 2000,   3000,   4000]
f = Frame(relief = RAISED, borderwidth = 5) #네모 프레임
var = StringVar()
for i, station in enumerate(stations): #프레임 안에 4개의 정류장 radio 버튼 생성
    radio = Radiobutton(f,
                       text = station,
                       variable = var,
                       value = i,
                       command = change)
    radio.pack(side = TOP)
f.pack(pady = 10)

var.set(0) #초기값
win.mainloop()
```



# 5일차 widget 처리 고급기법

> 목표 : for문 연동하여 위젯 배치 단순화, 리스트화, validation or tracing
>
> 내용 : for문 활용 배치 효율화, 값의 추적, 유효성검사

## 1. for loop 활용 위젯 배치

- 단순 배치시

```python
from tkinter import *
win = Tk()

titles = ('이름', '전화번호', '주소', '이메일', '소속', '회사전화')
for i in range(6):
    lbl = Label(win, padx = 20, text = titles[i]+':')
    lbl.grid(row = i*2, column = 0, padx = 40, sticky = 'nw')
```

- 변수가 필요시

```python
from tkinter import *
win = Tk()
titles = ('이름', '전화번호', '주소', '이메일', '소속', '회사전화')
tx = []
for i in range(6):
    tx.append(Entry(win, text = ''))
    tx[i].grid(row = i*2, column = 1, columnspan = 2, sticky = 'new')
```

- 인덱스 전송 필요시 (예 : 버튼)

```python
from tkinter import *
win = Tk()
def on_click(idx):
    print(prints[idx])
        
titles = ('추가', '수정', '삭제', '찾기', '종료', '리셋')
prints = ('add', 'update', 'delete', 'search', 'close', 'reset')
btn = []
for i in range(6):
    btn.append(Buttpn(win, width = 12, height = 2, text = titles[i], command = lambda p = i : on_click(p))) #p는 지역변수
    btn[i].grid(row = 10, column = i, padx = (20,0), pady = (45, 10), sticky = 'w')
```

## 2. 위젯 값 추적 하기 - 제어변수(2)

> v.tace(mode, callback) 메서드로 제어변수와 콜백함수를 연결

- 'r' : 변수 read시
- 'w' : 변수 write시
- 'u' : 변수 unset시

```python
def calㅣback(*args):
    print("variable changed!")
var = StringVar()
lbl = Label(win, text = "파이썬", textvariable = var).pack()
var.trace("w", callback)
var.set("hello")
```

### 제어 변수를 활용하여 위젯 값 추적

```python
from tkinter import *
def changed(e, m, c):
    s = sv.get()
    ln = len(s)
    print(s, ln)
def from_setting():
    global sv
    win = Tk()
    sv = StringVar()
    ent = Entry(win, textvariable = sv)
    ent.pack()
    ent.focus_set()
    return win
main = form_setting()
main.mainloop()

#sv.trace_add("write", callback) #트레이스 추가  
```

## 3. 유효성(validate) 검사

> 유효성 검사후 입력을 수용 or 거부 가능
>
> 대상 : Entry, ttk.combobox

### 순서

1. 검증 함수 작성

   ```python
   def validate_routine(t):
       lbl['text'] = t
       return True
   ```

2. register메서드를 이용해 검증함수 등록

   ```python
   vcom - win.register(validate_routine)
   ```

3. validate 옵션으로 검사시기를 지정

   ```python
   e1 = Entry(win, bd = 5, validate = "key", validatecommand = (vcom, '%S'))
   ```

4. validatecommand로 콜백함수 (2번등록함수)와 옵션지정



### 세팅 내용

#### 검사 시기 validate = "option"

- focus, focusin, focusout: 
- key : 키 입력으로 위젯 내용 변경 시
- all, none

#### 검사 옵션 validatecommand(검증함수, '%option')

- i : 위치
- P : 후문자열
- s : 전문자열
- S : 삽입 또는 삭제 문자열
- V : 상기 발생사유
- W : 발생위젯

```python
from tkinter import *
win = Tk()
def validate_routine(t):
    lbl['text'] = t
    return  True
'''
    if t.isnumeric():
        return True
    else:
        return False
'''
win.title('샘플프로그램')
vcom = win.register(validate_routine)
e1 = Entry(win, bd = 5, validate = 'key', validatecommand = (vcom, '%S')).pack
lbl = Entry(win, bd = 'red', fg = 'white', font = '굴림 20 bold').pack(fill = 'both')
e1.focus_force()
win.mainloop()
#return 액션을 안하면 원하는 결과 X
```

# 6일차 파일데이터 widget에 적재하기

> 목표 : 대량데이터 처리방식 이해, 리스트박스의 선택에 반응처리, 스크롤바와 다른 widget연동, 텍스트박스의 특징 tag 활용
>
> 내용 : 리스트박스 위젯, 파일로부터 데이터 적재, 스크롤바 위젯

## 1. Listbox

> w = Listbox(master, ....)
>
> 여러개의 텍스트 항목을 줄 단위로 표시, 사용자가 선택

### 옵션

- activestyle : 표시형식(underline, dotbox, none)
- listvariable : 제어변수 지정, get()과 set()메서드 활용
- selectmode : BROWSE, SINGLE < MULTIPLE, EXTENDED
- xscrollcommand, yscrollcommand : scrollbar 위젯과 연결 사용

### 메서드

- xview(), yview() : scrollbar 위젯과 연결 사용

```python
from tkinter import *
win = Tk()

lbox = Listbox(win)
lbox.insert(1, '가')
lbox.insert(2, '나')
lbox.insert(3, '다')

lbox.pack()
win.mainloop()
```

- 제어변수 활용하기

```python
from tkinter import *
win = Tk()

v = StringVar() #제어변수 선언
lbox = Listbox(win, listvatiable = v) # 생성시 변수연계
v.set('가 나 다 라 마') #제어변수 활용 : v.set('가....')
lbox.pack()
win.mainloop()
```

- 반복문 연동

```python
from tkinter import *
win = Tk()
people = ['가', '나', '다', '라', '마']
lbl = Label(win, text = '이름', relief = RAISED, bg="white")
lbl.pack()
lst = Listbox(win)
lst.pack(side = LEFT, fill = Y)

for data in people:
    lst.insert(END, data) #0부터 시작하는 정수값, 상수 END는 맨뒤, 상수 ANCHOR는 위치 포인터 앞(선택문자열이 있는 경우 그 앞)
win.mainloop()
```

## 2. 파일로부터 읽어 GUI연동

전화번호.txt

가, 010-1234-5678, 서울, 아파트

나, 010-1111-2222, 부산, 빌라

```python
f = open('전화번호.txt', 'r')
basedata = f.read()
f.close()
data = basedata.split('\n')

for j in range(len(data)):
    person = data[j].split(',')
    lst.insert(END, person)
```

## 선택에 반응

- lst.curselection() : 선택 요소의 라인번호 반환(튜플)
- lst.get(index) : 주어진 index 값 반환
- 응용과제 : 선택확인 버튼 누르면 레이블에 내용 출력

```python
from tkinter import *

def read_from_file():
    f = open('전화번호.txt', 'r')
    base = f.read()
    f.close()
    data = base.split('\n')
    for j in range(len(data)):
        person = data[j].split(',')
        lst.insert(END, person)

def form_setting():
    global lst, lbl
    win = Tk()
    lbl = Label(win, text = '이름', relief = RAISED, bg = 'white')
    lbl.pack(fill = BOTH)
    lst = Listbox(win, width = 60)
    lst.pack(side = LEFT, fill = Y)
    btn = Button(win, test='선택확인', command = select_one) #선택하는 버튼과 커맨드 추가
    btn.pack(anchor=N)
    return win

def select_one(): #선택하는 버튼함수 추가
    try:
        sel = lst.curselection()
        one = lst.get(sel)
        s = str(sel[0]) + '번 -->' + str(one)
        lbl.configure(text = s)
    except:
        return
main = form_setting()
read_from_file()
main.mainloop
    
```

## 3. Scrollbar

> w = Scrollbar(master, ...)
>
> Listbox, Text, Canvas 등과 연결하여 스크롤 콜트롤 위젯 구현에 사용

### 옵션

- command : 스크롤 발생시 실행 함수 지정
- jump : command 콜백 호출방식 >>> 드래그시마다 - 0, 놓을때 -1
- orinet : 가로세로 스크롤타입(HORIZONTAL, VERTICAL)
- throughcolor : 슬라이더 색상

### 메서드

- set() : 다른 위젯과 연결시, 다른 위젯의 xscroll, yscroll를 이 메서드에 설정

### scrollbar 와 다른 위젯(ex:listbox) 연동방법

1. List의 yscrolcommand에 Scollabr.set
2. Scrollbar command = List.yview

```python
from tkinter import *
master = Tk()

sbar = Scrollbar(master)
sbar.pack(side = RIGHT, fill = Y)
lbox = Listbox(master, yscrollcommand = sbar.set) #1번
for i in range(1000):
    lbox.insert(END, str(i))
    lbox.pack(side = LEFT, fill = BOTH)
sbar.config(command = lbox.yview) #2번
mainloop()
```

## 4. Text

> w = Text(master, ...)
>
> 여러 줄 텍스트를 입력 편집가능한 위젯

### 옵션

- spacing1, spacing2, spacing3 : 줄간격(위, 논리, 아래)
- Tabs : 탭키로 이동할 간격지정(cm)
- Undo, maxundo
- wrap : 단어 줄바꿈 or 문자 줄바꿈 지정(WORD, CHAR)
- **Xscrollcommand, yscrollcommand : 수평 수직 스크롤 설정(scrollbar의 .set()메서드 사용)**

```python
from tkinter import *

win = Tk()

fr = Frame(win)
tx = Text(fr, width = 40)
tx.pack(side = LEFT)

sc = Scrollbar(fr)
sc.pack(side = RIGHT, fill = Y)
sc.config(command = tx.yview)

tx.config(yscollcommand = sc.set)

fr.pack(side = 'left', fill = 'y')

win.geometry('300x200')
win.mainloop()
```

### 메서드

- compare(idx1, op, idx2) : 위치값 비교
- delete(idx1, idx2=None)
- get(idx1, idx2=None)
- tag_add(tagname, idx1, idx2=None)

### 문자입력 위치 지정자

- 'line.column', 'line.end'
- INSERT, END, CURRENT, SEL_FIRST, SEL_LAST

## 5. tag

> 특정문자나 단어에 표식을 붙여 글꼴, 색상, 크기, 함수호출등을 효율화

### 관련 메서드(=작업순서)

1. tag_add(tagname, idx1, idx2 = None)
2. tag_config(tagname, 옵션)
3. tag_blind(tagname, 이벤트타입, 함수)

예

```python
text.insert(INSERT, '고구려 팔만대장경')

1. text.tag_add('kor', '1.0', '1.3')#태깅 r.c
2. text.tag_config('kor', bg = 'yellow', foreground = 'blue', font = '굴림 14 bold')#태깅한것 모양설정
```

```python
from tkinter import *
win =Tk()
txt = Text(win)

txt.insert(INSERT, "고구려 팔만대장경")
txt.insert(END, "대한민국 알본.....미국")
txt.tag_add('kor', '1.0', '1.3')
txt.tad_add('start', '1.9', '1.14')

txt.insert(INSERT, '네이버', 'a')
txt.insert(INSERT, '서울특별시', 'b')
txt.pack()

txt.tag_config('kor', 설정1)
txt.tag_config('start', 설정2)
txt.tag_config('a', 설정3)
txt.tag_config('b', 설정4)
win.mainloop()
```

```python
from tkinter import *
import webbrowser
win =Tk()

def m_enter(e):
    print('마우스 인')
def m_leave(e):
    print('마우스 아웃')
def m_click(e):
    print('마우스 클릭')
txt = Text(win)

txt.insert(INSERT, "고구려 팔만대장경")
txt.insert(END, "대한민국 알본.....미국")
txt.tag_add('kor', '1.0', '1.3')
txt.tad_add('start', '1.9', '1.14')

txt.insert(INSERT, '네이버', 'a')
txt.insert(INSERT, '서울특별시', 'b')
txt.pack()

txt.tag_config('kor', 설정1)
txt.tag_config('start', 설정2)
txt.tag_config('a', 설정3)
txt.tag_config('b', 설정4)

txt.tag_blind('a', '<Enter>', m_enter)
txt.tag_blind('a', '<Button-1>', lambda e : webbrowser.open('http://www.naver.com/'))
txt.tag_blind('kor', '<Enter>', m_enter)
txt.tag_blind('start', '<Leave>', m_leave)
txt.tag_blind('kor', '<Button-1>', m_click)
txt.config(cursor = "arrow")
win.mainloop()
```

# 7일차 이벤트핸들링(1)

> 목표 : 이벤트와 구동방식 이해, 위젯의 이벤트 구분, event handler 작성가능, 위젯 bind method를 사용하여 이벤트와 처리기 연결가능
>
> 내용 : 위젯 이벤트 종류 (activate, deactivate, map, unmap, configure, destroy....), event binding, event add

- GUI OS 구동방식은 이벤트에 기반

- 운영체제나 어플리케이션 입장에서 event는 사용자의 의도를 감지한 신호체계

- 이러한 signal을 적절히 활용 >>> 사용자 편리성 증진

- 버튼 클릭 대응 방식의 한계

  ```python
  def click_event():
      pass
  b = Button(win, text = '확인', command = click_event)
  ```

  - 마우스 버튼을 눌러야만 작동
  - 발생 원인이 한 가지, parameter X >>> 다양한 처리 불가

```python
from tkinter import *
from tkinter import messagebox

win = Tk()
def ok_click():
    na = txt.get() #변경
    lbl2.configure(text = "당신의 이름은" + na +"입니다.")
    messagebox.showinfo("이름", na)
    
lbl = Label(win, text = "이름 : ")
lbl.grid(row = 0, column = 0)
txt = Entry(win, bg = "yellow")
txt.grid(row = 0,  column = 1)

btn = Button(win, text = "완료", command = ok_click)
btn.grid(row = 0, column = 2)

lbl2 = Label(win, text = "당신의 이름은 : ")
lbl2.grid(row = 2, column = 0, columnspan = 2, sticky = W)
win.bind('<Return>', lambda e : ok_click()) #엔터키 반응
txt.focus()
win.mainloop()
```

## Widget Events

- Activate : state가 활성 상태로 변경시(맥시스템)

- Deactivate : state가 비활성 상태로 변경시(맥시스템)

- Map : 창이 오픈 or 위젯이 팩될떄

- Unmap

- Configure : 위젯의 사이즈 변경시

- Destroy : 위젯 소멸시(X 버튼)

- Expose : 위젯의 가시성 변경 시

- FocusIn, FocusOut : 포커스 변경시

- KeyPress, KeyRelease, Enter, Leave, Button등 : 키보드, 마우스 관련

  조작되어있는 이벤트

- ListboxSelect : 리스트 항목이 선택되었을때

- Modified : 텍스트 등이 수정될 때

## event binding

> w.bind(even_name, handler[,+])

- 위젯을 이벤트에 바인딩시 사용

- 포커스 & 이벤트 발생 시, 지정된 핸들러 실행

- 내용, 환경의 변화, 키보드, 마우스, 타이머 등의 다양한 이벤트 바인딩 가능

  ```python
  def character_handler( event ): #파라미터
      pass
  txt1.bind('k', character_handler) #바인딩 >>> 키보드 k가 눌리면
  ```

  ```python
  from tkinter import *
  from tkinter import ttk
  
  def press_handler(e):
      lbl['text'] = '키보드가 눌렸습니다.'
  win = Tk()
  
  lbl = ttk.Label(win,
                 text = "키보드를 누르세요",
                 font = '굴림 20')
  lbl.bind('<Key>', press_handler) #'<Key>', 'a', <lines>
  #'a' or 'b' : 각각 바인딩 해줘야 한다
  #연속 ab : 'ab' 바인딩
  lbl.pack()
  lbl.focus()
  win.mainloop()
  ```

  ### 동일한 사항에 대한 핸들러 추가 바인딩

  ```python
  #w.bind(event_name, handler, '+')
  
  lbl.bind('<Key>', press_handler)
  lbl.bind('<Key>', press_handler2, '+')
  ```

  ```python
  from tkinter import *
  from tkinter import ttk
  
  def press_handler(e):
      lbl['text'] = '키보드가 눌렸습니다.'
  def press_handler2(e):
      lbl['background'] = 'yellow'
  win = Tk()
  
  lbl = ttk.Label(win, text = "키보드를 누르세요", font = '굴림 20')
  
  lbl.bind('<Key>', press_handler)
  lbl.bind('<Key>', press_handler2, '+')
  
  lbl.pack()
  lbl.focus()
  win.mainloop()
  ```

  ```python
  import tkinter as tk
  win = tk.Tk()
  text = tk.Text(win, width = 40, height = 20)
  text.pack(side = 'top', fill = 'both', expand = True)
  
  label = tk.Label(win, anchor = 'w', bg = 'red', fg = 'white')
  label.pack(side = 'bottom', fill = 'x')
  
  def Modif_event(event):
      ln = len(text.get("1.0", "end")) - 1
      label.configure(text = "%s 글자" % ln)
      text.edit_modified(False)#flag 세팅 중요
      
  text.bind('<<Modified>>', Modif_event)
  win.mainloop()
  ```

  **textvarialbe 위력 & FocusIn 이벤트**

  > 4 Entry에 같은 문자에 

  ```python
  from tkinter import *
  win = Tk()
  sv = StringVar()
  
  def focus_event(e):
      ent.select_range(0, len(sv.get()))
  
  ent = Entry(win, textvariable = sv).pack()
  ent.bind('<FocusIn>', focus_event)
  # Entry >>> tab키를 이용하면 어느곳이든 focus
  ent2 = Entry(win, textvariable = sv).pack()
  ent3 = Entry(win, textvariable = sv).pack()
  ent4 = Entry(win, textvariable = sv).pack()
  win.mainloop()
  ```

  ```python
  from tkinter import *
  data = ["가", "나", ...]
  def select_ine(a):
      try:
          sel = lst.curselection()
          one = lst.get(sel)
          lbl.configure(text = '선택' + str(sel[0]) + '번....' + one)
      except:
          return
  win = Tk()
  lbl = Label(win, text = '    ', bg = 'yellow', width = 20)
  lbl.pack(side = TOP, anchor = W)
  lst = Listbox(win)
  lst.pack(side = LEFT, fill = Y)
  
  for dt in data:
      lst.insert(END, dt)
      
  lst.bind('<<ListboxSelect>>', select_one) #새롭게 추가
  win.mainloop()
  ```

  

# 8일차 이벤트핸들링(2)

> 목표 : 이벤트 클래스 활용, virtual event 작성, event 강제 발생
>
> 내용 : listboxselected, comboboxselected, virtual event, event generation

- `<<` `>>`  : virtual event

- ```python
  from tkinter import *
  basedata = '''이름, 010-1111-2222, 주소, 직장'''
  data = basedata.split('\n')
  
  '''파일형식
  f = open('전화번호.txt', 'r')
  basedata = f.read()
  f.close()
  data = basedata.split('\n')
  '''
  
  def select_one(e=''):
      try:
          sel = lst.curselection()
          one = lst.get(sel)
          s = str(sel[0]) + '번 ..' + str(one)
          lbl.configure(text = s)
      except:
          return
  win = Tk()
  lbl = Label(win, text = '선택하세요', relief = RAISED, bg = 'white', justify = LEFT, width = 60)
  lbl.pack(anchor = W)
  
  lst = Listbox(win, width = 60, relief = RAISED)
  
  lst.pack(seif = LEFT, fill = Y)
  btn = Button(win, text = '선택확인', command = select_one)
  btn.pack(anchor = N)
  lst.bind("<<ListboxSelect>>", select_one)
  
  for j in range(len(data)):
      person = data[j].split(',')
      lst.insert(END, person)
  win.mainloop()
  ```

  ```python
  import tkinter as tk
  from tkinter import ttk
  
  data = [기업이름들]
  root = tk.Tk()
  
  tk.Label(root, text = '업체 선택', bd=3).grid(row = 0, colunn = 0)
  var_data = tk.StringVar()
  cb = ttk.Combobox(root, values = data, justify = "center", textvariable = var_data)
  cb.bind('<<ComboboxSelected>>', lambda ev : lbl.config(text = var_data.get()))
  #ev 사용안하지만 안 받으면 에러
  cb.grid(row = 0, column = 1)
  
  lbl = tk.Label(root, text = 'Not Selected', width = 15, bg = 'red', fg = 'white')
  lbl.grid(row = 0, column = 2)
  
  root.mainloop()
  ```

  사전활용 두 개 콤보 연동

  ```python
  from tkinter import *
  from tkinter import ttk
  data1 = {'1반':(사람들),}
  
  root = Tk()
  root.geometry('350x200')
  
  def comb1_selected(e): #1반 첫번째 사람이 default값
      v = var.get()
      comb2.config(values = data1[v])
      var2.set(data1[v][0])
  
  var = StringVar()
  comb1 = ttk.Combobox(root, textvariable = var)
  comb1.config(values = tuple(data1.keys()))
  comb1.grid(row = 0, column = 0)
  var2 = StringVar()
  comb2 = ttk.Combobox(root, textvariable = var)
  comb1.grid(row = 0, column = 1)
  
  comb1.bind("<<ComboboxSelected>>", comb1_selected)
  #comb1.current(0) #실행시키자마자 선택되어있기 원하면 >>> 이벤트는 발생 X
  #comb1.event_generate("<<ComboboxSelected>>") #이벤트 로딩도 강제로
  root.mainloop()
  ```

## 1. virtual event (가상이벤트)

> 일종의 개발자 정의형 이벤트
>
> 활용 : 2개 이상의 이벤트를 묶어서 하나의 핸들러에 바인딩
>
> `<<` virtual event `>>`

### 작업순서

1. 이벤트 정의 : `win.event_add('<<Myevent>>', '<Button-1>', '<Return>' ....)`
2. 이벤트 바인딩 : `btn.bind('<<Myevent>>', evt_handle)`

## 2. 강제 이벤트

> w = event_generate(event) : 이벤트를 강제로 발생시킨다

```python
datasource='''김동현, 010-2203-4000, 상계동 437, 한도양행, abc@abc.co.kr
 박은애, 010-0900-9988, 동작동 456, 삼명전자, bcd@kbx.co.kr
 최은주, 010-2200-4499, 마장동 444, 유일양행, afb@kkk.co.kr
 이동주, 010-5566-6688, 독산동 222, 열국전자, ccc@ooo.co.kr'''

datasource=datasource.split("\n")
for i in range(len(datasource)):
     datasource[i]=datasource[i].split(",")

print(datasource)     
point = 0

from tkinter import *
win=Tk()

def move(point):
    data[0]['text'] = datasource[point][0] 
    data[1]['text'] = datasource[point][1]
    data[2]['text'] = datasource[point][2]
    data[3]['text'] = datasource[point][3]
    data[4]['text'] = datasource[point][4]

win.geometry('400x200+500+500')
win.title(" 전화번호부")

def  inspec_r(e): #좌우로 이동하되 끝이면 동작 X
    global point
    ln=len(datasource)
    point += 1
    if point>= ln: point= ln-1
    move(point)
    
def  inspec_l(e):
    global point
    point -= 1
    if point<= 0: point= 0
    move(point)
win.bind('<Right>',  inspec_r)
win.bind('<Left>',  inspec_l)


                                  
f1 = Frame(win)
f1.pack(side = 'right', ipadx = 50)
label_texts = ('이름 :', '전화번호 :', '주소 :','소속 :', '이메일 :')
data = []

for r in range(5):
     Label(f1, text = label_texts[r], font="굴림 12" ).grid(column = 0, row = r,sticky = E)

     data.append(Label(f1, text = '...', font="굴림 12"))
     data[r].grid(column = 1, row = r, sticky = W)
     
btn=Button(win, text ="    >>    ", command = lambda:win.event_generate("<Right>"))
btn.pack()

move(point)
win.mainloop()
```

화살표 키를 눌렀을때 or 화면 버튼 클릭시 데이터 순환 디스플레이

방법1

```python
def btn_click():
    win.event_generate('<Right>')
btn = Button(win, text = ">>", command = btn_click)
```

방법2

```python
btn = Button(win, text = ">>", command = lambda : win.event_generate("<Right>"))
```

방법3

```python
def inspec_r(e =""):#로 변경 >>> 버튼은 파라미터 X
btn = Button(win, text =">>", command = inspec_r)
```

Tag에 binding

- Text 위젯

- > t.tag_bind(tagname, eventType, handler)

관련 메서드(=작업순서)

1. tad_add(tagname, idx1, idx2=None)
2. tag_config(tagname, 옵션)
3. tag_bind(tagname, 이벤트타입, 함수) #1,2는 기존에 학습

```python
from tkinter import *
import webbrowser
win = Tk()
def m_enter(e):
   print("마우스 들어왔음")
def m_leave(e):
   print("마우스 떠났음")
def m_click(e):
   print("마우스 클릭")
txt = Text(win)
txt.insert(INSERT, "고구려 팔만대장경")
txt.insert(END, "대한민국 일본.....미국")
txt.tag_add("kor", "1.0", "1.3")
txt.tag_add("start", "1.9", "1.14")
txt.insert(INSERT, "네이버 바로가기", "a")
txt.insert(INSERT, "서울특별시", "b")
txt.pack()
txt.tag_config("kor", background="yellow", foreground="blue",font="굴림 14 bold")
txt.tag_config("start", background="red", foreground="white", font="굴림 18 bold")
txt.tag_config("a", foreground="blue", underline=1)
txt.tag_config("b", background="green", foreground="white" )
txt.tag_bind("a", "<Enter>", m_enter)

#"a"태그에 Enter키가 들어오면 m_enter를 콜백하도록 tag_bind

txt.tag_bind("a", "<Button-1>", lambda e:webbrowser.open('https://www.naver.com/'))
txt.tag_bind("kor", "<Enter>", m_enter)
txt.tag_bind("start", "<Leave>", m_leave)
txt.tag_bind("kor", "<Button-1>", m_click)
txt.config(cursor="arrow")
win.mainloop()


move(point)
win.mainloop()
```

# 9강 키보드 & 마우스 이벤트

> 목표 : 키보드,마우스의 이벤트 특징을 이해하고 처리, 타이머 이벤트 활용
>
> 내용 : keyboard event type, key name, event calss, event modifiers

## 1. 키보드 이벤트

### 키보드 event Type & Keyname

- 키보드 이벤트 type : '<Key>', '<KeyPress>', '<KeyRelease>'

- 키 name : Keysym, Keysym_num, Keycode

### 이벤트 핸들러에 전달된 데이터 확인하기 (event class)

> char, keysym, keysym_num, keycode, serial, time, type, widget

```python
from tkinter import *
from tkinter import ttk

def label_change(e): #전달되는 데이터 출력으로 확인해보는 함수
    lbl['text']= e.keysym + "  "  + str(e.keysym_num) + "  " + str(e.keycode)
win=Tk()
lbl=Label(win, text="키보드를 누르세요", font="굴림 20", width=20)
win.bind("<KeyPress>", label_change)
lbl.pack()
win.mainloop() 
```

### event modifiers(복합키)

> Alt, Control, Lock (caps lock on), Shift, Double, Triple

`win.bind("<Control-Alt-Delete", 함수) `

```python
from tkinter import *
win = Tk()
    
def   ok_click():
    na=txt.get()
    lbl2.configure(text="당신의 이름....." + na )
lbl=Label(win, text="이    름 : ").grid(row=0, column=0)
txt=Entry(win, bg="yellow")
txt.grid(row=0, column=1)

btn=Button(win, text="완  료", command=ok_click)
btn.grid(row=0, column=2)

lbl2=Label(win, text="")
lbl2.grid(row=2,column=0, columnspan=2, sticky=W)
txt.focus()

win.bind("<KeyPress Return>", lambda  e: ok_click()) #e는 사용하지 않지만 받아줘야 에러 X
#이름 입력 후 리턴키에 반응하도록 추가(편리)

win.mainloop()
```

## 2. 마우스 이벤트

### 마우스 event Type & Name

- 마우스 event Type : 'Enter', 'Leave', 'Motion' : 마우스 포인터가 위젯 내에서 이동
- 마우스 event Name
  - `<1>`, `<2>`, `<3>` : 좌버튼, 휠버튼, 우버튼
  - `<Double-1>`, ... : 각 버튼 더블 클릭
  - `<ButtonRelease-1>`, ... : 각 버튼 눌렸다가 놓일 떄
  - `<B1-Motion>`, ... : 누른상태에서 끌때
  - `<MouseWhell>` : 마우스 휠이 가동 될 때

- event handler에 전달되는 값
  - num : 1,2,3
  - x, y : 위젯의 좌상단 모서리에서 측정한 좌표
  - x_root, y_root : 화면의 좌상단 모서리에서 측정한 좌표 **기준점 차이 조심**
  - state : 시프트(1), 콘트롤(4), 알트(131071) 등 특수키가 눌려 있는지

```python
from tkinter import *
from tkinter import ttk

def move_object(e): #클릭한 버튼 이동시키는 함수
       e.widget.place(x = e.x_root-win.winfo_x()-8,   
                               y = e.y_root-win.winfo_y()-30)
win = Tk()
win.geometry('600x380+500+500')
for c in range(6):
    lab = ttk.Button(win, text = str(c))
    lab.place(x = 0, y = c*30)
    lab.bind('<B1-Motion>', move_object)

win.mainloop()
```

```python
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry('200x200')

def   show_tooltip(e): #툴팁 보이기/숨기기 구현한 함수
    lab1.place(x=20, y=30)
def   hide_tooltip(e):
    lab1.place_forget()
    
b1=ttk.Button(win, text="불러오기")
b1.place(x=10,y=10, width=100)
b1.bind('<Enter>', show_tooltip)
b1.bind('<Leave>', hide_tooltip)

lab1=Label(win, bg='white', text='파일로부터 불러옵니다', relief=SOLID, bd=1)
lab1.place_forget()

win.mainloop()

```

```python
from tkinter import *

def trace_mouse(e): # 좌표값을 계속 출력해주는 함수
    lab1['text'] = '('+str(e.x)+','+str(e.y)+')'

def inter_zone(e): # 레이블 출입시 호출되는 함수
    but1['text'] = t1
def outer_zone(e):
    but1['text'] = t2

win = Tk()
win.geometry('300x180+500+500')

t1 = "버튼 위에 마우스 있음"
t2 ="버튼밖에 마우스"
lab1 = Label(win, font='굴림 14 bold')
lab1.pack()

but1 = Button(win, font='굴림 14 bold', text = t2)
but1.pack()

but1.bind('<Enter>', inter_zone)
but1.bind('<Leave>', outer_zone)
win.bind('<Motion>', trace_mouse)
win.mainloop()

```

```python
from tkinter import *

win = Tk()
win.geometry('150x150')

def in_event(e):
     e.widget['bg']='yellow'
def out_event(e):
     e.widget['bg']='white'
   
txt1= Entry(win)
txt1.grid(row=0, column=0)
txt1.bind('<FocusIn>', in_event) #txt1과 txt2가 같은 역할의 이벤트 핸들러 공유
txt1.bind('<FocusOut>', out_event)

txt2= Entry(win)
txt2.grid(row=1, column=0)
txt2.bind('<FocusIn>', in_event)
txt2.bind('<FocusOut>', out_event)
```

## Timer 이벤트

- 특정 시점 or 설정시간 간격으로 이벤트 발생

- 모든 창 or 위젯 클래스에는 시간 이벤트를 설정 메서드 보우

- 일종의 알람

  

- after(delay, fucntion[, *paras]) : delay 밀리초 후에 함수 (기능)을 호출

- after_cancel(event_id) : 이벤트를 취소

```python
from tkinter import *
switch= 0

def change_color( ):
    global switch
    if switch:
        win['background']='yellow'
    else:
        win['background']='green'
        
    lab1['text'] = win.cget('background')  
    lab1.after(1000, change_color) #바인딩과 동일 >>> 깜빡깜빡 기능  
    switch= not switch
    
win = Tk()
win.geometry('200x150')

lab1 = Label(win, text = 'Waiting')
lab1.pack()

lab1.after(1000, change_color) #바인딩과 동일

win.mainloop()
```

# 10강 mini project

> 목표 : 유저 관점에서 위젯을 효율적으로 배치하고 반응하는 프로그램 작성, 실세계에서의 경험적 이해가 가능한 item을 실제 Application에 작성에 적용하여 개발능력 제고
>
> 내용 : 위젯의 배치, 데이터 적재, 이벤트 바인딩과 핸들링, 선택에 반응과 처리