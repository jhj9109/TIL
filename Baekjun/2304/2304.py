import sys
sys.stdin = open('input.txt')

N = int(input())
pillars = [0]*1000
for _ in range(N):
    L, H = map(int, input().split())
    pillars[L] = H

max_index = 0
max_val = pillars[0]
result = 0

for i in range(1, 1000):
    if pillars[i] > max_val:
        result += (i - max_index) * max_val
        #print(f'앞무빙({i} - {max_index}   * {max_val})' )
        #print(result)
        max_val, max_index = pillars[i], i

max_index, mid_index = 999, max_index
max_val2 = 0
for i in range(999, mid_index-1, -1):
    if pillars[i] > max_val2:
        #print(f'뒷무빙s({max_index+1} - {i+1} * {max_val2})' )
        result += (max_index+1 - (i+1)) * max_val2
        max_val2, max_index = pillars[i], i
        
    if i == mid_index:
        #print(f'뒷무빙({max_index+1} - {i} * {max_val2}' )
        result += (max_index+1 - (i)) * max_val2
        
print(result)