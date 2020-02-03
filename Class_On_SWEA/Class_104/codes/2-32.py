#다음과 같이 사용자가 입력한 문장에서
#숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.

a=input() #str

num_str , num_int = 0, 0
for i in a:
    if i.isdigit() :
        num_int +=1
    elif 'a'<=i<='z':
        num_str +=1
    elif 'A'<=i<='Z':
        num_str +=1
print("LETTERS {0}".format(num_str))
print("DIGITS {0}".format(num_int))