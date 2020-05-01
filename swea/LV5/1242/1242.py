import sys
sys.stdin = open("input1242.txt")
def find_not_zero(data): # 배열속 코드 획득
    idx = 0
    while idx < M:
        if data[idx] != '0':
            get_bin_code( hex_to_bin(data) )
            return
        idx += 1

def hex_to_bin(data):
    bin_data = ''
    for d in data:
        bin_data += h[d]
    return bin_data

def get_bin_code(lst): # 배열속 2진코드 획득, 배수와 상관없이 1집합이 16이 된다.
    global codes
    idx = len(lst)-1
    cnt = 0
    while idx >= 0:
        # 0부터 존재
        while lst[idx] == '0' and idx >= 0:
            idx -= 1
        if idx == -1:
            break
        first = idx
        while lst[idx] == '1':
            idx -= 1

        while lst[idx] == '0':
            idx -= 1
        while lst[idx] == '1':
            idx -= 1
        
        while lst[idx] == '0':
            idx -= 1
        code_length = (first - idx) * 8
        codes.add(lst [first+1 - code_length  : first+1 ])

        idx = first - code_length

def trans(inputs): # 2진 암호코드를 해석
    global res
    temp = []
    i = 0
    interval = len(inputs) // 56
    while i < len(inputs):
        st = ''
        for _ in range(7):
            st += inputs[i]
            i += interval
        temp.append( k[st] )

    cnt = 0
    for i in range(len(temp)):
        cnt += temp[i] if i&1 else temp[i]*3
    if not(cnt % 10):
        res += sum(temp)

k = {
    '0001101':0,    '0011001':1,    '0010011':2,    '0111101':3,
    '0100011':4,    '0110001':5,    '0101111':6,    '0111011':7,
    '0110111':8,    '0001011':9,
}
h = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [ input() for _ in range(N) ]
    res = 0
    codes = set()
    for row_d in d:
        find_not_zero(row_d)
    for code in codes:
        trans( code )
    print(f'#{tc} {res}')