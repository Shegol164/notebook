from src.OOP_14_1.lesson_1.Album import  Album
from src.OOP_14_1.lesson_1.Bottle import Bottle
from src.OOP_14_1.lesson_1.Number import Number
from src.OOP_14_1.lesson_1.Student import Student

def main():
    album_1 = Album("Queen", "Killer Queen", ["Brighton rock", "Killer Queen", "Tenement Funster"])
    album_2 = Album("Metallica", "Black Album", ["Enter Sandman", "Sad But True", "Holier Than Thou"])
    print(album_1.artist, album_1.title, len(album_1.tracks), "треков")
    print(album_2.artist, album_2.title, len(album_2.tracks), "треков")
    print("*" * 119)

    bottle_1 = Bottle("Красная", 0.7)
    bottle_2 = Bottle("Белая", 0.3)
    bottle_3 = Bottle("Черная", 0.1)

    # код для проверки
    print(bottle_1.color, bottle_1.volume)  # Красная 0.7
    print(bottle_2.color, bottle_2.volume)  # Белая 0.3
    print(bottle_3.color, bottle_3.volume)  # Черная 1.0
    print("*" * 119)

    n = Number(7)
    print(n.get())  # 7
    n.add(3)
    print(n.get())  # 10
    n.substract(5)
    print(n.get())  # 5
    print("*" * 119)

    student_1 = Student("Алиса", 3)
    student_2 = Student("Маргарита", 2)
    print(student_1.name, student_1.course)  # Алиса 3
    print(student_2.name, student_2.course)  # Маргарита 2

if __name__ == "__main__":
    main()