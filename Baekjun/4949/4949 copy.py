import sys
sys.stdin = open('input.txt')

while True:
    data = sys.stdin.readline()
    # print(list(data))
    if len(data) == 1 and data[0] == '.':
        break
    else:
        s1, s2, flag = 0, 0, False
        last = 0
        for d in data:
            if d == "(":
                s1 += 1
            elif d == "{":
                s2 += 1    
            elif d == ")":
                if s1 != 0:
                    s1 -= 1
                else:
                    flag = True
                    break
            elif d == "}":
                if s2 != 0:
                    s2 -= 1
                else:
                    flag = True
                    break
        if flag or s1 != 0 or s2 != 0:
            print('no')
        else:
            print('yes')