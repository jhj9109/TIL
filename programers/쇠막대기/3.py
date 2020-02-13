def solution(arrangement):
    stack=0
    answer=0
    for i in arrangement:
        if i=="(":
            stack+=1
            cut=True
        else:
            stack-=1
            if cut:
                answer+=stack
                cut=False
            else:
                answer+=1
    return answer

data = input()
print(solution(data))