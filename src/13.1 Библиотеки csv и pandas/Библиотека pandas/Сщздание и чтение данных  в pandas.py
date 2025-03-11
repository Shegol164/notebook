"""Установка pandas"""
# poetry add pandas
"""Импорт библиотеки"""
# import pandas as pd

"""Основные объекты pandas"""
# DataFrame - это двумерная таблица, в которой каждая запись соответствует строке и столбцу. Она позволяет хранить и
# обрабатывать данные в табличной форме.
import pandas as pd
df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df)
print("#"*119)

df = pd.DataFrame({
    'Bob': ['Мне это понравилось.', 'Это было ужасно.'],
    'Sue': ['Довольно хорошо.', 'Без вкуса.']
})
print(df)
print("#"*119)

df = pd.DataFrame({
    'Bob': ['Мне это понравилось.', 'Это было ужасно.'],
    'Sue': ['Довольно хорошо.', 'Без вкуса.']
}, index=['Товар A', 'Товар B'])
print(df)
print("#"*119)

#Series— это одномерная последовательность значений данных. Напоминает столбец в таблице DataFrame.

s = pd.Series([1, 2, 3, 4, 5])
print(s)
print("#"*119)

s = pd.Series([30, 35, 40], index=['Продажи 2015 года', 'Продажи 2016 года', 'Продажи 2017 года'], name='Товар A')
print(s)
print("#"*119)

"""Чтение данных из файлов"""
"""Чтение данных из CSV-файла"""
# Функция pd.read_csv() — используется для чтения данных из CSV-файла.
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews)
print(wine_reviews.shape)
print(wine_reviews.head(3))
print("#"*119)

"""Чтение данных из Excel-файла"""
# Функция pd.read_excel() — используется для чтения данных из файла Excel.
# Для корректной работы с Excel-файлами в pandas необходимо дополнительно установить библиотеку openpyxl:
# poetry add openpyxl
excel_data = pd.read_excel("winemag-data-130k-v2.xlsx")
print(excel_data)
print(excel_data.shape)
print(excel_data.head())
print("#"*119)
# Выбор конкретного листа в Exel
xls = pd.ExcelFile("winemag-data-130k-v2.xlsx")
print(xls.sheet_names)  # Cписок листов

excel_data_specific_sheet = pd.read_excel("winemag-data-130k-v2.xlsx", sheet_name='Лист 2',)
print(excel_data_specific_sheet.head())