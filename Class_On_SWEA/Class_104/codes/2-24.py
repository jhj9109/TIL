"""
두 개의 리스트 [1,3,6,78,35,55]와 [12,24,35,24,88,120,155]를 이용해
양쪽 리스트에 모두 있는 항목을 리스트로 반환하는 프로그램을 작성하십시오
"""

d1 = [1,3,6,78,35,55]
d2 =[12,24,35,24,88,120,155]
d3 = set(d1) & set(d2)
d4 = list(d3)

print(d4)