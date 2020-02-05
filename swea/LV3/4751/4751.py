T = int(input())
for T in range(T):
    word = input().strip()
    n_word = [n for n in word]
    joint = '#.'+'.#.'.join(word)+'.#'

    sts1 = '#'*len(word)
    sts2 = '.'*(len(word)*2+1)
    sts1 = '..'+ '...'.join(sts1) + '..'
    sts2 = '#'.join(sts2)

    print(sts1)
    print(sts2)
    print(joint)
    print(sts2)
    print(sts1)