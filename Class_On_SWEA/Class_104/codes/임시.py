class Student:

    def __init__(self, name, gender, height , data3):
        self.__name = name
        self.__gender = gender
        self.__height = height
        self.__data3 = data3

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @property
    def data3(self):
        return self.__data3

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return "{0}(name: {1}, gender: {2}, height: {3}, date3: {4})"\
            .format(self.__class__.__name__, self.name, self.gender, self.height, self.data3)

#__repr__ 객체 출력시 주로 사용됨. 안내 멘트 느낌?
"""
students =  [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.5),
    Student("강감찬", "남", 182.2),
]

for student in students:
    print(student)

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=False):
    print(student)
"""