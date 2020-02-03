# 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
# 입력
# 홍길동
# 이순신
# 가위
# 바위
# 출력
# 바위가 이겼습니다!
def gababo(a,b):
    if a==b : print("%s가 이겼습니다!"%(a))
    else:
        if a!="가위" and b!="가위" :    print("보가 이겼습니다!")
        elif a!="바위" and b!="바위" :  print("가위가 이겼습니다!")
        else :                          print("바위가 이겼습니다!")
human1=input()
human2=input()
what1=input()
what2=input()
gababo(what1,what2)