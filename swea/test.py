#numbers =list(map(int, input().split(' ')))
numbers = [3,2,1,4]

sort_num = [0] * len(numbers)
cnt = [0]*(max(numbers)+1)
for number in numbers:
    cnt[number] += 1
for i in range(max(numbers)):
    cnt[i+1] += cnt[i]
for i in range(len(numbers)):
    cnt[numbers[i]] -= 1
    sort_num[cnt[numbers[i]]] = numbers[i]
print(sort_num)
