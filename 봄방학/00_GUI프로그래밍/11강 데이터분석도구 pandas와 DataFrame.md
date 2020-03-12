# 10강 mini project

- 목표

1. 유저 관점에서 위젯을 효율적으로 배치하고 반응하는 프로그램 작성
2. 실세계에서의 경험적 이해가 가능한 item을 실제 Application에 작성에 적용하여 개발능력 제고

- 내용

1. 위젯의 배치, 데이터 적재
2. 이벤트 바인딩과 핸들링
3. 선택에 반응과 처리



## 전화번호 프로그램

- 변수 all_records에 친구의 신상정보 (이름, 전화번호, 소속, 이메일)이 저장되어 있다
- 레코드별 리스트박스 위젯에 출력한다
- 리스트박스에서 선택된 레코드는 각각의 필드를 엔트리에 반영해 주어야한다.
- 엔트리에서 즉시 수정 후 수정버튼을 누르면 반영된다.
- 수정버튼 외에도 추가, 삭제, 검색 등 버튼을 구현한다.

### 폼 구성

> def setting_gui():

```python
all_records=[["박인덕", "010-1111-vvvv","aa","bb"], ["오수미", "010-2222-vvvv","cc","dd"],
          ["김인숙", "010-3333-vvvv","ee","ff"], ["최금혹", "010-4444-vvvv","gg","hh"],
          ["민동욱", "010-5555-vvvv","ii","jj"], ["성열휴", "010-6666-vvvv","kk","ll"],
          ["김동휘", "010-7777-vvvv","mm","nn"], ["이올석", "010-8888-vvvv","oo","zz"],
          ["김민규", "010-9999-vvvv","pp","qq"], ["홍길동", "010-1010-vvvv","rr","ss"],
          ["김민규", "010-1110-vvvv","tt","uu"]]   

from tkinter import *

def preparation():
    global pData, point
    pData = all_records
    point=0
    win.title('전화번호관리')
    setting_gui()
    setting_list()
    
def setting_list():
    for record in all_records:
         lst.insert(END,str(record[0] + ' ::  ' +record[1])) #모두가 아닌 일단 2개만 출력토록 구현해 놓음
    lst.focus_set()
    lst.selection_set(point)
    show_data(pData[point])
#----버튼 임시작업-------
def on_select(event): pass
def show_data(data):
def on_delete(): pass
def on_close(): win.destroy()
def on_search(): pass
def on_update(): pass
def on_add(): pass
def on_click(idx): pass
#-----------------------
def setting_gui(): # 폼작업
    global lst, tx, pData, tsearch
      #레이블 세팅
    titles=('이       름: ','전 화 번 호: ','주       소: ', 'Email: ')
    for i in range(4):
        lbl=Label(win, padx = 20,text= titles[i])
        lbl.grid(row = i*2, column = 0,  sticky = 'nw')
    lbl_user = Label(win,padx = 20, text = '이   름 / 전화번호 ')
    lbl_user.grid(row = 0, column = 2, sticky = 'nw')
      #엔트리 세팅  
    tx=[] 
    for i in range(4):
         tx.append(Entry(win, text = ''))
         tx[i].grid(row = i*2 +1, column = 0, columnspan = 2,  padx = 40, sticky = 'new')
    
    tsearch = Entry(win, text = '')
    tsearch.place(x=380, y=200)
      #스크롤& 리스트
    scrollbar1 = Scrollbar(win, orient = VERTICAL)
    lst = Listbox(win, exportselection = 0, yscrollcommand = scrollbar1.set)
    lst.bind('<<ListboxSelect>>', on_select)
    scrollbar1.config(command = lst.yview)
    scrollbar1.grid(row = 1, column = 5, rowspan = 7, sticky = 'nes')
    lst.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')
      #버튼  
    titles=('add', 'update', 'delete',' Search', 'Close')
    btn=[]
    for i in range(5):
        btn.append(Button(win,  width = 12, height = 2, text = titles[i], command= lambda ii=i :on_click(ii)))
        btn[i].grid(row = 8, column = i, padx = (20,0), pady = (45,10), sticky = 'w')

```

### 리스트 선택에 반응

> 리스트박스 내 특정항목 선택 시 실행될 bingding 함수

```python
'''
1.리스트박스 반환
2.선택된 인데스값 반환
3.선택된 인덱스를 이용해서 리스트원본(pData)에서 1인분을 꺼내온다
4.출력함수호출(1인분 요소를 보낸다 data)
'''
def on_select(event):
    id_list = event.widget
    selection_id = id_list.curselection()[0]
    data = pData[selection_id]
    show_data(data)
```

### 엔트리 출력

> 인자값으로 넘어온 리스트 항목을 각각 엔트리박스에 디스플레이
>
> (현재 엔트리 박스 내용을 지우고, 넘어온 1인분을 출력해 준다.)

```python
def show_data(data):
    for i in range(len(tx)): #이름, 번호, 주소, 이메일
        tx[i].delete(0, END) #지우고
        tx[i].insert(0, data[i]) #넣고
```

### 추가버튼 구현

> 엔트리박스내용을 리스트원본(pData) 및 리스트박스(lst) 맨 뒤에 추가해준다.

```python
'''
1.위치값변수(point)를 맨뒤로
2.리스트박스 선택해제
3.맨뒤를 리스트박스 선택항목으로
4.선택항목을 보이게한다(자동스크롤)
'''
def on_add():
    pData.append([tx[0].get(),tx[1].get(),tx[2].get(),tx[3].get()])
    lst.insert(END, tx[0].get() + " :: " + tx[1].get())
    point= len(pData)-1
    lst.selection_clear(lst.curselection())
    lst.selection_set(point)    
    lst.see(point) 
```

### 수정버튼 구현

> 엔트리 입력된 내용을 리스트원본(pData) 및 리스트박스(lst)에 반영

```python
'''
1. 기존에 데이터가 1개라도 있는 경우
2. 기존에 데이터가 1개도 없는 경우
>>>우선 빈데이터 append(인덱싱에러방지)
>>>엔트리에 있는 내용을 리스트원본과 리스트박스에 반영
'''
def on_update():
    ln=len(pData)
    if ln >= 1: #1
        point = lst.curselection()[0]
        lst.delete(point)
    else: #2
        point = 0
        pData.append(["","","",""])  #빈 리스트이므로 자리확보(인덱싱에러방지)

    for i in range(len(tx)):
        pData[point][i] = tx[i].get() #업데이트

    lst.insert(point, tx[0].get() + " :: " + tx[1].get())
    lst.selection_set(point)
    lst.see(point)
```

### 삭제버튼 구현

> 현재의 항목을 삭제

```python
'''
1. 데이터 갯수를 구한다
2. 데이터가 있는 경우만 작업한다
ex1) abcd 중 b 삭제 : b 삭제 C를 current로 (point 불변)
ex2) abcd 중 d 삭제 : b 삭제 C를 current로
ex3) a 삭제 : a 삭제후 빈 데이터 세팅
'''

def on_delete():
    ln=len(pData) #1
    if ln >= 1: #2
        point = lst.curselection()[0]
        pData.remove(pData[point])
        lst.delete(point)

        if point>=ln-1 : #ex2 & ex3
            point=point-1
        if point >= 0: #ex1
            data=pData[point]
            lst.selection_set(point)
        else:
            data = "","","",""
        show_data(data)     
```



### 찾기 버튼 구현

> 찾고자 하는 이름을 입력하면 엔트리와 리스트박스에 디스플레이 한다.

```python
'''
1.선택해제
2.새로운것 선택
3.선택항목을 보이게
'''
def on_search():
    
    sName= tsearch.get()
    found=False
    for i in range(len(pData)):
       
        if sName in pData[i]:
           p= i
           found=True #찾았으면
           break
    if found: #찾았으면
        show_data(pData[p])

        lst.selection_clear(lst.curselection()) #1
        lst.selection_set(p) #2
        lst.see(p) #3
```







# 11강 데이터분석도구 pandas와 DataFrame

- 목표

1. 파이썬 데이터 분석도구를 이해
2. pandas의 DataFrame 생성
3. DataFrame의 row, column 생성 및 추가, 삭제 등 처리
4. 요약통계 및 각 요소를 이해, 각각을 메서드로 호출
5. 조건을 주어 데이터를 filtering 처리

- 내용

1. pandas 소개
2. DataFrame 구조 이해
3. DataFrame 생성하기
4. 수치로 변환, 반올림, 명칭변경, 컬림의 추가, 삭제, 연산
5. 조건을 이용한 filtering

##  1. pandas란

> 데이터 분석능력을 겸비한 데이터 조작도구
>
> 테이블 구조로 다루며, 데이터 연산 집계 병합 정렬등 다양한 메서드 제공

### 데이터 사이언스를 위한 파이썬 라이브러리

- Numpy : 다차원 배열 및 행렬 대상 고급 수학 및 통계연산
- Scipy : 선형대수, 미분, 수치통합 등 과학적 연산
- Pandas : 데이터연산, 집계, 병합, 정렬등을 제공하는 데이터 분석도구
- SciKit-Learn : 분류 회기 클러스터링, 기계학습 알고리즘 제공

### Visualization 라이브러리

- matplotlib : histogram, bar, scatter 등 2D기반 plotting라이브러리 제공
- Seaborn : 고수준 통계그래픽 인터페이스 제공

## 2. pandas DataFrame

> row, column, data로 이루어진 테이블 데이터 구조
>
> 주요개발환경 : jupyter notebook (아나콘다 설치시 자동)

### DataFrame 만들기

1. 리스트로 만들기

2. 딕셔너리로 만들기

### 수치형 문자 숫자로 바꾸기

- 여러 필드 한꺼번에 : `df = df.apply(pd.to_numeric, errors = 'ignore')` 에러 발생시 ignore해!

- 특정 필드

  ```python
  df['국어'] = pd.to_numeric(df['국어'])
  df['영어'] = pd.to_numeric(df['영어'])
  df['불어'] = pd.to_numeric(df['불어'])
  ```

### 데이터 견본 보기 : df.head(2), df.tail(3)

### 데이터 구조(행열) 보기 : df.shape >>> (4, 4)

### 기본요약통계보기

- df.describe() : count, mean, std(편차), min, 25%, 50%, 75%, max
- df.mean() : 평균
- df.quantile(0.7)

### column 추가 / 연산

```python
df['총점'] = df['국어'] + df['영어'] + df['수학']
df['평균'] = df['총점'] / 3
df
```

```python
df['총점'] = df.sun(axis = 1)
df['평균'] = df[ ['국어', '영어', '수학'] ].mean(axis=1)
df
```

`df.assign(추가컬럼명 = [값....])`

### 소수점 이하 자릿수

- 여러 필드 한꺼번에

  ```python
  df = df.round(2)
  df
  ```

- 특정 필드

  `df = df.round( {'평균' : 2} )`

### column 명칭 변경

```python
df = df.rename(columns = {'수학' : '산수', '총점' : '합계'})
df
```

### index를 특정 컬럼으로 변경

```python
df = df.set_index('이름')
df
```

### filtering

- `df2 = df[df.합계 >= 170]; df2`

- `df['결과'] = ['합격' if x >= 60 else '불합격' for x in df.평균]; df`

- ```python
  import numpy
  df['수상여부'] = numpy.where(df['평균'] >= 85, '수상', '-')
  df
  ```

### column 추가

`df = df.assign(번호 = [1,2,3,4]); df`

### column 삭제

`df.drop('수상여부', axis = 1, inplace = True); df`

- axis : 1 - column 기준 작업
- inplace : True - 바로 작업

### 문제 : index를 '이름'에서 '번호'로 바꾸어라

1. 이름 컬럼을 추가

   ```python
   a = df.index
   df = df.assign(이름=a)
   df
   ```

2. 번호를 index로

   ```python
   df = df.set_index('번호')
   df
   ```

3. 순서를 매긴 뒤 재구성한다.

   ```python
   cols=['이름','국어', '영어','산수','합계','결과']
   df=df[cols]
   df
   ```

   

# 12강 pandas DataFrame(2) & GUI 연동

- 목표

1. DataFrame의 다양한 메서드를 이용하여 연산 및 조작
2. indexing과 slicing을 통해 특정 요소 참조 및 세팅
3. 처리결과를 GUI와 연동하여 출력

- 내용

1. DataFrame의 연산
2. column 추가, 명칭변경
3. indexing과 slicing / 특정요소의 참조 및 세팅
4. DataFrame 창에 출력하기

## 1. pandas DataFrame

### row, column 처리(인덱싱, 슬라이싱)

- column명을 이용한 선택
  -  `df['이름']` : 인덱스는 기본 
  - ``df[ ['이름'], ['국어'] ]` : 이름,국어를 하나로 만들어 넘기는것
- index를 이용한 row 선택 : `.loc[idx, col]` 
  - `df.loc[4, '국어']` 
  - `df.loc[ 4, ['국어', '영어', '산수' ] ]` 
  - `df.loc[2:4, :]` == `df.loc[2:4, ]` == `df.loc[2:4]`

- 위치값(숫자)을 이용한 선택 : `.iloc[r, c]`
  - `df.iloc[3] ` == `df.iloc[3, ]` == `df.loc[4]`
  - `df.iloc[0:2, 0:2]` 

### 문제 : 전체총점(세로합계)을 구하기

```python
#원하는 결과 안 나옴
df.loc['전체총점'] = df.sum(axis = 0)
df

#방법1 : 더할 값은 오직 숫자
df.loc['전체총점']=df.sum(axis=0, numeric_only=True)
df
#방법2 : 더할 column 지정하기
df.loc['전체총점', ['이름','국어', '영어','산수']] = df.sum(axis = 0)
df
```

### NaN값 바꾸기

```python
df.fillna('-', inplace = True)
df
```

- isna()
- notna()
- fillna()
- dropna()

## 2. DataFrane과 GUI 연동

### 도입 - 2차원 리스트 출력하기

```python
import tkinter as tk

data='''김인문, 010-2244-3545, 상계동 344, 한국기원
박동식, 010-4456-9988, 삼성동 699, 정보진흥사
최전문, 010-6600-0998, 역삼동 855, 삼명전자
박동훈, 010-5500-0922, 방학동 667, 엘우전자
이형호, 010-5621-2356, 구로동 577, 드림시스
한희훈, 010-5978-3434, 시흥동 522, 엠투게임
지동석, 010-2202-4508, 영등포 434, 엘우전자
황인숙, 010-2222-0909, 도봉동 333, 휘경분식
최철훈, 010-5649-0908, 보문동 342, 시네마천국
이미영, 010-5771-2956, 구로동 888, 드림미
한희훈, 010-5978-3434, 홍은동 112, 엠스탁
지동석, 010-2455-4608, 양재동 422, 우미타워
홍길동, 010-3333-5555, 경호동 333, 동우상사
창동원, 011-2222-3333, 민락동 444, 방배건설
최후민, 010-3333-8888, 하원동 222, 충성건설'''


def read_data(): #2차원 리스트 생성
     global data
     data=data.split('\n')
     
     for i in range(len(data)):
           data[i]= data[i].split(',')



def   display_list( d_frame ):
      
      rows=len(d_frame)
      cols= len(d_frame[0])
   
      for  rr  in range(rows):
             for  cc  in range(cols):
                   e = tk.Entry(width=15)
                   e.insert(0, d_frame[rr][cc])
                   e.grid(row=rr, column=cc)


win=tk.Tk()
read_data()
win.title(" 출력결과")
display_list( data )

```

### 확장 - pandas 출력 (리스트와 출력과 동일 원리)

- 문제 : 전화번호를 텍스트파일로 저장후 csv로 읽어 창에 출력하라

```python
import pandas as pd
import tkinter as tk
def read_data(): #읽어오기
    global  df #데이터 프레임
    try:
       df=pd.read_csv('전화번호.txt')
    except:
       df=pd.read_csv('전화번호.txt',encoding='CP949') #한글 인코딩 utf-8에 문제있으면 -> CP949
       
def display_title( d_frame): #제목출력루틴 (추가)
    title=list(d_frame.columns)
    e=tk.Entry(win, text=' ', width=10, bg='gray', fg='white')
    for  i  in range(len(title)):
         e = tk.Entry(win, width=10, bg='gray', fg='white')
         e.insert(0, title[i])
         e.grid(row=0, column=i+1) #column 출력은 1부터

def display_dataframe(d_frame): #def display_pandas와 동일
    rows, cols = d_frame.shape #.shape 이용해 len값 구하기
    for r in range(rows):
         e = tk.Entry(win, bg='gray',fg='white', width=10)
         e.insert(0, d_frame.index[r])
         e.grid(row=r+1,column= 0) #제목이 0줄 > r+1 , 인덱스 출력 col = 0

         for c in range(cols):
             e = tk.Entry(win, width=10)
             e.insert(0, d_frame.iloc[r,c]) #.iloc[r, c] syntax에러 조심 ^^
             e.grid(row=r+1, column=c+1)

win=tk.Tk()
read_data()
win.title(" 출력결과")
display_title(df)
display_dataframe(df)

win.mainloop()
```

### 제목출력루틴(추가)

```python
def display_title( d_frame):
    #위에 참조
```

### 예제 : tips.csv를 pandas로 읽어 출력하라

```python
import pandas as pd
import tkinter as tk
def   read_data():
    global data, df, pd
    df=pd.read_csv( "tips.csv") #읽어오기
    df=df.apply(pd.to_numeric, errors='ignore')

def display_title( d_frame): #재사용
    title=list(d_frame.columns)
    e=tk.Entry(win, text=' ', width=10, bg='gray', fg='white')
    for  i   in   range(len(title)):
         e = tk.Entry(win, width=10, bg='gray', fg='white')
         e.insert(0, title[i])
         e.grid(row=0,column=i+1) 


def display_pandas(d_frame): #재사용
    rows, cols = d_frame.shape
    for r in range(rows):
         e = tk.Entry(win, bg='gray',fg='white', width=10)
         e.insert(0, d_frame.index[r])
         e.grid(row=r+1,column= 0)

         for c in range(cols):
             e = tk.Entry(win, width=10)
             e.insert(0, d_frame.iloc[r,c])
             e.grid(row=r+1, column=c+1)

win = tk.Tk()

read_data()
win.title("처리결과")
display_title(df)
display_pandas(df)

win.mainloop()
```

# 13강 DataFrame & plotting 결과 GUI연동하기

- 목표

1. 처리결과를 분류, 여러창에 체계적 출력
2. matplotlib, seabornm, DataFrame 이용한 visualizaion의 기법의 기초 이해
3. 기본적이고 중요한 그래프의 종류와 사용목적 이해, 생성
4. visualization 결과를 GUI에 연동출력

- 내용

1. DataFrame, matplotlib, seaborn의 plotting 기법
2. histogram, scatter, boxplot 등 주요그래프 plotting
3. backend모듈과 연동하여 GUI창에 출력

## 여러 창에 data frame 출력하기

### parameter로 창을 넘겨받아 출력한다

```python
import pandas as pd
import tkinter as tk
def   read_data():
    global data, df, pd
    df=pd.read_csv( "tips.csv")
    df=df.apply(pd.to_numeric, errors='ignore')
#-------------wnd로 창을 넘겨 받는다-------------------------------------
#기존 단일 : win, 현재 각각의 wnd
def display_title(wnd, d_frame):
    title=list(d_frame.columns)
    e=tk.Entry(wnd, text=' ', width=10, bg='gray', fg='white')
    for  i   in   range(len(title)):
         e = tk.Entry(wnd, width=10, bg='gray', fg='white')
         e.insert(0, title[i])
         e.grid(row=0,column=i+1) 

def display_pandas(wnd, d_frame):
    rows, cols = d_frame.shape
     
    for r in range(rows):
         e = tk.Entry(wnd, bg='gray',fg='white', width=10)
         e.insert(0, d_frame.index[r])
         e.grid(row=r+1,column= 0)

         for c in range(cols):
             e = tk.Entry(wnd, width=10)
             e.insert(0, d_frame.iloc[r,c])
             e.grid(row=r+1, column=c+1)
#-------------wnd로 창을 넘겨 받는다----------------------------------
win = tk.Tk()

read_data()
win.title("처리결과")
display_title(win,df)
display_pandas(win, df)

#-------------df.describe()메서드-------------------------------------
win2= tk.Tk()
win2.title('기초통계 요약')
df2=df.describe()
display_title(win2, df2)#df2로 바꿔야한다는데 안바꿔도...?
display_pandas(win2, df2)

win3= tk.Tk()
win3.title('소숫점 자릿수 조정')
df3=df2.round(2)
display_title(win3, df3)
display_pandas(win3, df3)


win5= tk.Tk()
win5.title('팁 6$ 이상 고객')
df5=df[df.tip>=6]
display_title(win5, df5)
display_pandas(win5, df5)


win.mainloop()
```

## Data frame 조작 & 창 출력 실습

### df.describe() 메서드

> data frame의 기초 통계를 보여준다 

## 시각화하기

### 그래프 종류

- 막대그래프 : 상대비교

  ```python
  df2 = df.head(10)
  plt.bar(df2.index, df2['tip'])
  ```

- 히스토그램 : 데이터분포

  `plt.hist(df['tip'])`

- 산점도 : 두 변수간 관계

  `plt.scatter(x = 'total_bill', y = 'tip', data = df)`

- 박스플롯 : 범주형 데이터 분포표현

  `plt.boxplot(df['tip'])`

- 커널밀도추정차트(kde) : 데이터분포와 밀도

  `sns.joinplot(x = 'total_bill', y = 'tip', data = df, kind = 'kde')`

### DataFrame객체 활용

`df.plot(x = 'total_bill', y = 'tip', kind = 'scatter')`

### matplotlib모듈 활용

```python
import matplotlib.pyplot as plt
plt.scatter(x = 'total_bill', y = 'tip', data = df)
```

### seaborn모듈 활용

```python
import seaborn as sns
sns.sactterplot(x = 'total_bill', y = 'tip', data = df)
```

### 초간단 시각화 작업순서

1. import : `import matplotlib.pyplot as plt`

2. data 준비 : `import seaborn as sns`

3. 스타일 지정, 제목, 레이블 모양갖추기 (선택)

   ```python
   # matplot폰트 깨지는 문제 이슈 해결 위함
   import matplotlib.font_manager as fm
   path = 'C:\windows]Fonts\폰트.TTF' #내 컴퓨터에 맞게 수정
   font_name = fm.FontProperties(fname = path, size = 20).get_name()
   plt.rc('font', family = font_name) #font 이름 넘겨주기
   plt.grid(linestyle = '-')
   plt.title('식대별 팁 보기')
   plt.xlabel('식대')
   plt.ylabel('팁')
   ```

4. 그리기 : `plt.scatter(y = 'tip', x = 'total_bill', data = df, c = 'blue')`

5. 보여주기 : `plt.show()`

### 모양 갖추기 메서드

- `plt.title('graph title')` : 그래프 제목
- `plt.ylabel('y축 값 설명')` : y축 설명
- `plt.xlabel('x축 값 설명')` : x축 설명
- `plt.legend(loc = '위치')` : 범례
- `plt.xlim(x축 최소, x축 최대)` : x축 최대, 최소값 지정
- `plt.ylim(y축 최소, y축 최대)` : y축 최대, 최소값 지정