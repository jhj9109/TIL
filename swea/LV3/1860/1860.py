#import sys

#sys.stdin = open("input.txt", "r")
T = int(input())
data1 = list()
for T in range(T):
    N, M, K = list(map(int, input().strip().split()))

    humans = list( (n//M) for n  in map(int, input().strip().split()))
    result = 'Possible'

    cnt = dict.fromkeys(sorted(humans),0)
    
    for human in humans:
        cnt[human] += 1

    sum_cnt = 0
    sum_people = 0
    for i, v in cnt.items():
        sum_cnt += v
        if i * K < sum_cnt:
            result = "Impossible"
            break

    
    print(f'#{T+1} {result}')

#     if result == "Impossible":
#         data1.append('#'+str(T+1))
# #print(data1)
# sys.stdin = open("output.txt", "r")
# data2 = list()
# for _ in range (1000):
#     temp = (input().strip().split()) #str
#     if temp[1] =="Impossible":
#         data2.append(temp[0])

# #print(data2)
# print(len(data1))
# print(len(data2))
# for val in data2:
#     if val not in data1:
#         print (val)