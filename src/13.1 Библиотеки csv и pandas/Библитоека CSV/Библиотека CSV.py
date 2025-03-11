# Формат CSV (Comma-Separated Values — значения, разделенные запятыми) — это текстовый формат, широко используемый
# для хранения табличных данных, где каждая строка файла соответствует строке таблицы, а ячейки в строке разделены
# специальным символом-разделителем, чаще всего запятой.
"""Пример содержимого CSV-файла:
Name,Age,Gender
Alice,25,Female
Bob,30,Male
Charlie,35,Male"""
import csv

rows = [['Name', 'Age', 'Gender'],
        ['Alice', '25', 'Female'],
        ['Bob', '30', 'Male'],
        ['Charlie', '35', 'Male']]

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

"Чтение из CSV-файла"
import csv

with open('file.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print("#"*119)

"""Работа с CSV как со словарями"""
# Функция DictReader — позволяет читать CSV-файл и создавать словари из строк файла. Ключами в словаре будут названия
# столбцов, а значениями — значения в соответствующих ячейках.

# Пример чтения с DictReader:
import csv

with open('file.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'], row['Gender'])
print("#"*119)

#Функция DictWriter — позволяет записывать словари в CSV-файл.
import csv

rows = [{'Name': 'Alice', 'Age': '25', 'Gender': 'Female'},
        {'Name': 'Bob', 'Age': '30', 'Gender': 'Male'},
        {'Name': 'Charlie', 'Age': '35', 'Gender': 'Male'}]

with open('Файл CSV из  словаря .csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'Gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

"""Пример работы с CSV-файлом"""
import csv

with open('students.csv') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # Пропускаем заголовок таблицы
    for row in reader:
        name, age, avg_grade = row
        if float(avg_grade) > 4.5:
            print(f'{name} ({age} лет) - средний балл: {avg_grade}')