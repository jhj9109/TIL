프로그래머스 스킬 테스트1

``` python
def solution(word):

    if 'p' not in word and 'y' not in word:
        return True
    
    cnt = 0
    for ch in word:
        if ch == 'p' or ch == 'P':
            cnt += 1
        if ch == 'y' or ch == 'Y':
            cnt -= 1
        
    if cnt == 0 :
        return True
    else:
        return False
```

```python
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) + "에 있다"
```
