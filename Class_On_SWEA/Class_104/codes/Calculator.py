num1=int(input("첫번째숫자:"))
num2=int(input("두번째숫자:"))
operator=str(input("사칙연산기호:"))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else :
    print("%s : 잘못입력하셨습니다" % operator)
2