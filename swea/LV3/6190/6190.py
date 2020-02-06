import sys
sys.stdin = open("input.txt")
'''
swea를 믿지 않으니, 인풋값 NN은 쓰지 않음
N 정수 갯수
multis : 주어진 정수 2개를 택해 곱한 값(중복선택X) 내림차순 정렬
각 multi에 접근해 뒷자리부터 나머지와 몫을 이용해 단조증가여부 검사
'''
# T = int(input())
# for tc in range(1, T+1):
#     NN = int(input())
#     data = list(map(int, input().split()))
#     N = len(data)
#     multis = sorted([data[x] * data[y] for x in range(N-1) for y in range(x+1,N)], reverse=True)
#     for multi in multis:
        
#         i = 1
#         previous_digit = multi % (10 ** i)

#         while multi // (10 ** i) != 0:
#             i += 1
#             next_digit = (multi % (10 ** (i))) // (10 ** (i-1))
#             if previous_digit < (multi % (10 ** (i))) // (10 ** (i-1)):
                
#                 break
#             else:
#                 previous_digit = next_digit
#         else:
#             print(f'#{tc} {multi}')
#             break
#     else: 
#         print(f'#{tc} -1')

#밑에 아직 수정중
def myfunc_digit(num, N):
    return (num % (10 ** (N))) // (10 ** (N-1))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    result = -1
    for idx_1 in range(len(num_list) - 1):
        for idx_2 in range(idx_1 + 1, len(num_list)):
            current_num = num_list[idx_1] * num_list[idx_2]
            n = 1
            previous_digit = myfunc_digit(current_num, n)
            while current_num // (10 ** n) != 0:
                n += 1
                next_digit = myfunc_digit(current_num, n)
                if previous_digit < next_digit:
                    break
                previous_digit = next_digit
            
            else:
                result = current_num
    print('#{0} {1}'.format(tc, result))