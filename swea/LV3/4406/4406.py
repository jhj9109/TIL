T = int(input())
for T in range(T):
    word = input().strip()
    n_word = [n for n in word if n not in 'aeiou']
    #print(''.join(n_word))
    print('#{} {}'.format(T+1, ''.join(n_word)) )