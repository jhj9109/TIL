"""ej코드
test_num = int(input())
 
for i in range(test_num):
    dict_new_nums = dict.fromkeys(['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'], 0)    
 
    this_test, length = input().split()
 
    nums = input().split()
    for num in nums:
        dict_new_nums[num] += 1
         
    print(f'#{i+1}')
    for key, val in dict_new_nums.items():
        for _ in range(val):
            print(key, end = ' ')
"""
T = int(input())
for T in range(T):
    x, N = input().split()
    N = int(N)

    data = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    test = list(input().strip().split())
    new_test = [0 if st == data[0] else 1 if st == data [1]\
                else 2 if st == data[2] else 3 if st == data [3]\
                else 4 if st == data[4] else 5 if st == data [5]\
                else 6 if st == data[6] else 7 if st == data [7]\
                else 8 if st == data[8] else 9 for st in test]
    sorted_test = sorted(new_test)
    print('#{}'.format(T+1))
    for num in sorted_test:
        print(data[num], end=' ')
    print('')