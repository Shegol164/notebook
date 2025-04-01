from src.OOP_14_1.lesson_2.bankacount import BankAccount
from src.OOP_14_1.lesson_2.person import Person
from src.OOP_14_1.lesson_2.rectangle import Rectangle
from src.OOP_14_1.lesson_2.user import User


def main():
    # код для проверки
    account = BankAccount(1000)
    print(account.balance)  # 1000

    account.deposit(500)
    print(account.balance)  # 1500

    account.withdraw(200)
    print(account.balance)  # 1300

    account.close()
    print(account.balance)  # 0
    print("*" * 119)

    # код для проверки
    person1 = Person("John", 28)
    person1.display()  # John is 28 years old

    person2 = Person.from_birth_year("Mike", 1995)
    person2.display()  # Mike is 26 years old

    print(Person.is_adult(20))  # True
    print(Person.is_adult(15))  # False
    print("*" * 119)

    # код для проверки
    rectangle = Rectangle(4, 5)
    print(f"Площадь прямоугольника: {rectangle.area()}")  # 20
    print(f"Периметр прямоугольника:{rectangle.perimeter()}")  # 18

    rectangle2 = Rectangle.from_diagonal(5, 2)
    print(rectangle2.area())  # 10.0128
    print(rectangle2.perimeter())  # 13.42

    print(Rectangle.is_square(4, 4))  # True
    print(Rectangle.is_square(4, 5))  # False
    print("*" * 119)

    user1 = User("Alice", "qwerty")
    print(user1.name)  # Alice
    print(user1.password)  # qwerty
    print(user1.is_admin)  # False

    user1.password = "newpassword"
    print(user1.password)  # newpassword

    user1._is_admin = True
    print(user1.is_admin)  # True

    user1.login("newpassword")  # True
    user1.logout()

if __name__ == "__main__":
    main()