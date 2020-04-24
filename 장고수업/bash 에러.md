# git bash python permission denied windows

>  깃배쉬에서 python 명령어 permission denied 발생 (pip명령어도 동일)

## python 설치 경로 

- C:\Users\jangh\AppData\Local\Microsoft\WindowsApps\Python 3.8

- C:\Users\jangh\AppData\Local\Microsoft\WindowsApps\Python 3.8\scripts\

## 참조 링크

- https://stackoverflow.com/questions/56974927/permission-denied-trying-to-run-python-on-windows-10

- https://stackoverflow.com/questions/32597209/python-not-working-in-the-command-line-of-git-bash?noredirect=1&lq=1

## 환경 변수

- 사용자 변수 > PATH
  - %USERPROFILE%\AppData\Local\Microsoft\WindowsApp
- 시스템 변수 > PATH
  - C:\Users\jangh\AppData\Local\Programs\Python\Python38\
  - C:\Users\jangh\AppData\Local\Programs\Python\Python38\scripts\

## .bashrc 별명

- `alias python="winpty python.exe"`
- `alias pip="winpty pip.exe"`

## 상황1

- 사용자 변수 X & 시스템 변수 X & .bashrc 별명 등록 X
- cmd
  - python X : 'python'은 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
    배치 파일이 아닙니다.
  - pip X : 'pip'는 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
    배치 파일이 아닙니다.
- bash
  - python X : python : command not found
  - pip실행 X : pip : command not found

## 상황 2

- 사용자 변수 X & 시스템 변수 O & .bashrc 별명 등록 X
- cmd
  - python O
  - pip O
- bash
  - python ? : python 이름.py run O, python 실행시 무슨 동작인지 모르겠음
  - pip O

## 상황 3

-  사용자 변수 O & 시스템 변수 X & .bashrc 별명 등록 X

- cmd
  - python O
  - pip O
- bash
  - python : bash: /c/Users/jangh/AppData/Local/Microsoft/WindowsApps/python: Permission denied
  - pip : bash: /c/Users/jangh/AppData/Local/Microsoft/WindowsApps/pip: Permission denied

## 상황 4

- 사용자 변수 O & 시스템 변수 X & .bashrc 별명 등록 O
- bash
  - python O
  - pip X : python이 실행되는 기적이...
    - pip install django==2.1.15 명령어 입력시
      - C:/Users/jangh/AppData/Local/Microsoft/WindowsApps/pip.exe: can't open file 'install': [Errno 2] No such file or directory > 

## 상황 5

- 사용자 변수 O & 시스템 변수 O & .bashrc 별명 등록 O
- cmd > echo %PATH%
  - **C:\Users\jangh\AppData\Local\Programs\Python\Python38\;C:\Users\jangh\AppData\Local\Programs\Python\Python38\scripts\;**C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\Git\cmd;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\sqlite;**C:\Users\jangh\AppData\Local\Microsoft\WindowsApps;**C:\Program Files\Bandizip\;C:\Users\jangh\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\jangh\AppData\Roaming\npm;

- bash
  - python O
  - pip O

## 결론

- 시스템 변수 path 등록과 .bashrc 별명 등록으로 해결
- 참조 링크에서 봤던 windowapp 과의 충돌이 문제?

- pip 혹은 bash가 권한 받아야하는 폴더에 생길 경우 발생하는 현상 (윈도우 기준) (comment by john)