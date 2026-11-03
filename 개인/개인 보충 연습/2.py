# class Person:
#     population = 0

#     def __init__(self, name):
#         self.name = name
#         Person.population += 1

#     @classmethod
#     def get_population(cls):
#         print(cls.population)

        
# # p1 = Person("홍길동")
# # p2 = Person("김철수")
# # p3 = Person("이영희")

# # Person.get_population()       
# class Calculator:

#     @staticmethod
#     def add(a,b):
#         return a + b 

# result = Calculator.add(10, 20)

# print(result)        

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"저는 {self.name}이고 {self.age}살입니다.")


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        super().introduce()
        print(f"{self.school} 학생입니다.")

student = Student("홍길동", 20, "SSAFY")

student.introduce()

