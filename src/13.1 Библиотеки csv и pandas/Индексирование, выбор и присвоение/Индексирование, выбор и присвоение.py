import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

"Обращение к данным по строкам через индексацию"
# iloc (Integer Location) — позволяет осуществлять доступ к данным по их числовым индексам или позициям.
#reviews.iloc[0]              # Первая строка датафрейма
#reviews.iloc[:, 0]           # Первый столбец датафрейма
#reviews.iloc[:3, 0]          # Первые три строки первого столбца
#reviews.iloc[1:3, 0]         # Вторая и третья строки первого столбца
#reviews.iloc[[0, 1, 2], 0]   # Первые три строки первого столбца
#reviews.iloc[-5:]            # Последние пять строк датафрейма

# loc (Label Location) — позволяет осуществлять доступ к данным по их меткам или именам.
#reviews.loc[0, 'country']     # Значение первой строки в столбце `country`
#reviews.loc[:, 'country']     # Все значения в столбце `country`
#reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]  # Все значения в указанных столбцах
# Синтаксис
# dataframe.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)

import pandas as pd

data = {
    'student_id': ['001', '002', '003'],
    'name': ['Alice', 'Bob', 'Charlie'],
    'grade': [87, 92, 78]
}

df = pd.DataFrame(data)

# Установить 'student_id' в качестве индекса
df.set_index('student_id', inplace=True)

# Легкий доступ к данным конкретного студента
print(df.loc['001'])
print("#"*119)

"""Отбор данных по условию"""
italy_reviews = reviews.loc[reviews.country == 'Italy']
print(italy_reviews)
print("#"*119)

"""Объединение условий с помощью логических операторов"""
# Использование логического оператора & (и)
high_rating_italy_reviews = reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
print(high_rating_italy_reviews)
print("#"*119)
# Использование логического оператора | (или)
italy_or_high_rating_reviews = reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
print(italy_or_high_rating_reviews)
