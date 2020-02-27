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
옵션 : tearoff 뜯어내기 T/F, tearoffcommand 알림받기, command 메뉴 선택시 실시할 함수 지정

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