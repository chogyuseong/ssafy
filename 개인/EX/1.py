# class UserInfo:
#     def __init__(self):
#         self.user_data = {}

#     def get_user_info(self):
#         """
#         사용자로부터 이름과 나이를 입력받습니다.
#         - 이름이 없거나 공백이면 None을 반환합니다.
#         - 나이가 숫자가 아니거나 입력되지 않으면 ValueError를 처리하고 False를 반환합니다.
#         - 올바르게 입력되면 사용자 정보를 저장하고 True를 반환합니다.
#         """
#         name = input("이름을 입력하세요 : ")

#         if name.strip() == "":
#             return None

#         try:
#             age = int(input("나이를 입력하세요 : "))

#             self.user_data = {
#                 "이름": name,
#                 "나이": age
#             }

#             return True

#         except ValueError:
#             print("나이는 숫자로 입력해야 합니다.")
#             return False

#     def display_user_info(self):
#         """
#         저장된 사용자 정보를 출력합니다.
#         - 정보가 없으면 "사용자 정보가 입력되지 않았습니다."를 출력합니다.
#         """
#         if self.user_data:
#             print("사용자 정보 :")
#             print(f"이름 : {self.user_data['이름']}")
#             print(f"나이 : {self.user_data['나이']}")
#         else:
#             print("사용자 정보가 입력되지 않았습니다.")


# # 아래 코드는 수정하지 마세요.
# user = UserInfo()
# result = user.get_user_info()

# if result is True:
#     user.display_user_info()
# elif result is None:
#     user.display_user_info()

# class Animal:
#     def speak(self):
#         print("동물이 소리를 냅니다.")

# class Dog(Animal):
#     def speak(self):
#         print("멍멍")

# class Cat(Animal):
#     def speak(self):
#         print("야옹")


# animals = [
#     Dog(),
#     Cat(),
#     Animal()
# ]

# for animal in animals:
#     animal.speak()

# class Character:
#     count = 0

#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

#         Character.count += 1

#     def status(self):
#         print(f'이름 : {self.name}, HP : {self.hp}')

#     @classmethod
#     def show_count(cls):
#         print(cls.count)

# class Warrior(Character):

#     def __init__(self, name, hp, attack):
#         super().__init__(name, hp)
#         self.attack = attack

        
#     def status(self):
#         print(f'이름 : {self.name}, HP : {self.hp}, 공격력 : {self.attack}')

# w1 = Warrior("용사", 100, 30)
# w2 = Warrior("기사", 120, 40)

# w1.status()
# w2.status()

# Character.show_count()

# class Employee:
#     Employee_count = 0 

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#         Employee.Employee_count += 1 

#     def introduce(self):
#         print(f'이름 : {self.name}, 연봉 : {self.salary}')

#     @classmethod
#     def show_employee_count(cls):
#         print(cls.Employee_count)


# class Developer(Employee):

#     def __init__(self, name, salary, language):
#         self.language = language
#         super().__init__(name, salary)

#     def introduce(self):
#         print(f'이름 : {self.name}, 연봉 : {self.salary}, 주 언어 : {self.language}')


# dev1 = Developer("홍길동", 5000, "Python")
# dev2 = Developer("김철수", 6000, "Java")

# dev1.introduce()
# dev2.introduce()

# Employee.show_employee_count()


# text = input()
# words = text.split()
# number = len(words)


# print(f'문자열을 입력하세요 : {text}')
# print(f'대문자 : {text.upper()}' )
# print(f'소문자 : {text.lower()}' )
# print(f'단어 개수 : {number}')

# text = input()
# star = text.startswith("P")
# end = text.endswith("3")
# count = 0

# for a in text:
#     if a.isdigit():
#         count += 1

# print(f'숫자의 개수 : {count}')

# if text.isdigit():
#     print("숫자로만 이루어져 있습니다.")
# else:
#     print("숫자로만 이루어져 있지 않습니다.") 


# if star:
#     print(f'P로 시작합니다.')
# else:
#     print(f'P로 시작하지 않습니다.')

# if end:
#     print(f'3으로 끝납니다.')
# else:
#     print(f'3으로 끝나지 않습니다.')

a = int(input("숫자입력"))

if a == 3:
    print(f'a 는 {a}이다')

elif a == 7:
    print("행운의 숫자")

else:
    print("흥미로운 숫자")



