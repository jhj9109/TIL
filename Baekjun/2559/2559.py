N, K = map(int,input().split())
temps = list(map(int, input().split()))
#print(temps)
max_result, result = sum(temps[0:K]), sum(temps[0:K])
for i in range(K, N):
    result += temps[i] - temps[i-K]
    #print(result)
    max_result = result if result > max_result else max_result
print(max_result)