"""
리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
"""
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
data_list = [fibo(i) for i in range(1,11)]
print(data_list)