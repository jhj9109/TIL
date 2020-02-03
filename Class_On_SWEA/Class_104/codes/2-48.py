"""
가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.
"""


class Rectangle:

    def __init__(self, a,b):
        self.__a = a
        self.__b = b
    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def area(self):
        return self.a * self.b


rectangle = Rectangle(4,5)
print("사각형의 면적: {0}".format(rectangle.area()))