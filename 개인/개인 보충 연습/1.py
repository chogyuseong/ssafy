# class Dog ():
#     legs = 4 

#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def bark(self):
#         print(self.sound)

# dog1 = Dog("멍멍이", "멍멍")
# dog2 = Dog("초코", "왈왈")

# print(dog1.legs)
# print(dog2.legs)

# dog1.bark()
# dog2.bark()


# class Car:
#     wheels = 4

#     def __init__(self, brand, engine):
#         self.brand = brand
#         self.engine = engine

#     def drive(self):
#         print("달리는 중!")
#         return self.engine


# car = Car("Hyundai", "V6")

# result = car.drive()
# print(result)

# class Student:
#     school  =   "SSAFY"

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def introduce(self):
#         print(f"안녕하세요. 저는 {self.name}입니다.")

#     def is_pass(self):
#         if self.score >= 60 : 
#             return True
#         else: return False    

# student1 = Student("홍길동", 80)
# student2 = Student("김철수", 45)

# student1.introduce()
# student2.introduce()

# print(student1.is_pass())
# print(student2.is_pass())

# print(student1.school)


# class BankAccount:

#     bank = "SSAFY Bank"

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             return True
#         else: return False

#     def show_balance(self):
#         print(f"현재 잔액은 {self.balance}입니다.")    


# account = BankAccount("홍길동", 5000)

# account.deposit(3000)
# account.show_balance()

# print(account.withdraw(1000))
# account.show_balance()

# print(account.withdraw(10000))
# account.show_balance()

# class book:
#     category = "IT"

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def introduce(self):
#         print(f"책 제목: {self.title} 저자 : {self.author} 가격 : {self.price}")

#     def discount(self, percent):
#         self.price = self.price - (self.price * percent/100)

#     def is_expensive(self):
#         if self.price >= 30000:
#             return True
#         else: return False

# book = book("파이썬 기초", "홍길동", 20000)
# book.introduce()
# book.discount(10)

# print(book.is_expensive())
# print(book.category)

class GameCharacter:
    game = "Python RPG"

    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp =   hp

    def info(self):
        print(f"이름 : {self.name} 레벨 : {self.level} HP : {self.hp}")

    def level_up(self):
        self.level += 1 
        self.hp += 20

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0 :
            self.hp = 0

    def is_alive(self):
        if self.hp > 0:
            return True
        elif self.hp == 0:
            return False

character = GameCharacter("용사", 5, 100)

character.info()

character.level_up()
character.info()

character.take_damage(30)
character.info()

print(character.is_alive())
print(character.game)
            

