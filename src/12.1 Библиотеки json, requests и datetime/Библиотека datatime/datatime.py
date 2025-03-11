import datetime

# Создание объекта datetime для 8 марта 2022 года, 15:45:00
date_obj = datetime.datetime(2022, 3, 8, 15, 45, 0)
print(date_obj)
print("#" * 119)

"""Атрибуты объекта datetime"""
if __name__ == "__main__":
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    hour = date_obj.hour
    minute = date_obj.minute
    second = date_obj.second
    print(year, month, day, hour, minute, second)
print("#" * 119)
"""Форматирование дат и времени"""
if __name__ == "__main__":
    date_string = date_obj.strftime("%d-%m-%Y %H:%M:%S")
    print(date_string)
print("#" * 119)
"""Получение текущей даты и времени"""
if __name__ == "__main__":
    current_date_time = datetime.datetime.now()
    print(current_date_time)
print("#" * 119)
"""Изменение даты и времени"""
if __name__ == "__main__":
    date_obj = datetime.datetime(2022, 3, 8)
    new_date_obj = date_obj.replace(year=2023, month=3, day=8)
    print(new_date_obj)
print("#" * 119
