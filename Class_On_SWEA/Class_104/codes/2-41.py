"""
사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고,
중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.
산 하늘 강 바다 하늘 강 들

"""
data0=input()
data1=data0.split(" ")

data2=set(data1)
data3=sorted(list(data2))

for d in data3:
    if d != data3[len(data3)-1]: 
        print("{0}".format(d),end=",")
    else:
        print(d)


