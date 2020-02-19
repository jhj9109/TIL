import sys
sys.stdin = open('input.txt')

while True:
    data = sys.stdin.readline()
    if len(data) == 1 and data[0] == '.':
        #print('종료')
        break
    else:
        s, flag = [], False
        for d in data:
            if d == "(" or d == "[":
                s.append(d)
            elif d == ")":
                if len(s) == 0 or s.pop() != "(":
                    flag = True
                    break
            elif d == "]":
                if len(s) == 0 or s.pop() != "[":
                    flag = True
                    break
        if flag or len(s) != 0:
            print('no')
        else:
            print('yes')