# _*_ coding: utf-8 _*_

#8강 함수로 원 둘레 면적 구하기

print("원의면적 : {0:0.2f}".format(3.14*5*5))

#위 코드를 함수화

def input_radius():
    radius_str = input("반지름을 입력하세요:")
    return float(radius_str)

def calc_circle_area(r):
    return 3.14 * r * r

circle_area=calc_circle_area(5)

print("원의면적 : {0:0.2f}".format(circle_area))

radius=input_radius()
circle_area2=calc_circle_area(radius)
print("원의면적 : {0:0.2f}".format(circle_area2))