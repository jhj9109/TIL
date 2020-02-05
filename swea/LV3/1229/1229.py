def my_insert(idx):
    for i in range(order[idx+2]):
        test.insert(order[idx+1]+i,order[idx+3+i])

def my_pop(idx):
    for _ in range(order[idx+2]):
        test.pop(order[idx+1])

def my_append(idx):
    for i in range(order[idx+1]):
        test.append(order[idx+2+i])
"""
1.N
2.원본
3.N
4.명령어 (문자 + 숫자세트)

I : [x]위치에 y개의 숫자(s....)를 삽입 .insert(x,값) > 1개씩 가능
0    1        2         3 .......
D : [x]위치에 y개의 숫자 삭제 .pop(인덱스)/.remove(x)
0    1        2 
A : 맨뒤에 y개의 숫자(S....)를 삽입 .append
0          1         2......
"""

T = 10
for T in range(T):
    N1 = int(input().strip())
    test = list(map(int, input().strip().split()))
    N2 = int(input().strip())
    order = [n if 'A' <= n <= 'Z' else int(n) for n in input().strip().split()]

    
    for idx, val in enumerate(order):
        if val == 'I':
            my_insert(idx)
        if val == 'D':
            my_pop(idx)
        if val == 'A':
            my_append(idx)
    
    print('#{} '.format(T+1),end='')
    for i in range(10):
        print(test[i], end=' ')
"""춘화's
def convert_password(password,command):
    command_idx, start_idx, len_idx, value_idx = 0, 1, 2, 3
    result = password[:]
    while start_idx < len(command):
        command_key = command[command_idx]
        insert_idx = int(command[start_idx])
        value_len = int(command[len_idx])
        if command_key == 'I':
            insert_list = command[value_idx:value_idx+value_len]
            front_pass, back_pass = result[:insert_idx], result[insert_idx:]
            result = front_pass + insert_list + back_pass
            start_idx += (3+value_len)
            command_idx = start_idx-1
            len_idx = start_idx+1
            value_idx = start_idx+2
        elif command_key == 'D':
            result = result[:insert_idx] + result[insert_idx+value_len:]
            start_idx += 3
            command_idx = start_idx-1
            len_idx = start_idx+1
            value_idx = start_idx+2
        elif command_key == 'A':
            add_len = int(command[command_idx +1])
            add_idx = command_idx + 2
            result.extend(command[add_idx:add_idx+add_len])
            start_idx += (2+add_len)
            command_idx = start_idx-1
            len_idx = start_idx+1
            value_idx = start_idx+2
    return result
 
for tc in range(1,11):
    len_password = int(input())
    temp = input().split(' ')
    while True:
        if '' in temp:
            temp.remove('')
        else:
            break
    password = temp[:]
    len_command = int(input())
    temp = input().split(' ')
    while True:
        if '' in temp:
            temp.remove('')
        else:
            break
    command = temp[:]
    password = convert_password(password,command)
    print(f'#{tc}',*password[:10])
--------------------경득
T = 10
 
for test_case in range(1, T + 1):
    a = int(input())
    numbers = list(map(int, input().split()))
    b = int(input())
    c = input().split()
    for i in range(b):
        if c[0] == 'I':
            c.pop(0)
            x = int(c.pop(0))
            length = int(c.pop(0))
            for j in range(length):
                numbers.insert(x+j, int(c.pop(0)))
        elif c[0] == 'D':
            c.pop(0)
            x = int(c.pop(0))
            it = int(c.pop(0))
            for _ in range(it):
                numbers.pop(x)
        elif c[0] == 'A':
            c.pop(0)
            it = int(c.pop(0))
            for J in range(it):
                numbers.append(int(c.pop(0)))
    print(f'#{test_case}', end=' ')
    print(*numbers[0:10])
"""