import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

"""Использование метода isin"""
# Метод isin — проверяет, содержится ли значение в определенном столбце в заданном списке значений.
italy_france_reviews = reviews.loc[reviews.country.isin(['Italy', 'France'])]
print(italy_france_reviews)
print("#"*119)

"""Использование метода notnull"""
# Метод notnull — проверяет, является ли значение в столбце не равным NaN (неопределенным или отсутствующим).
not_null_price_reviews = reviews.loc[reviews.price.notnull()]
print(not_null_price_reviews)
print("#"*119)

"""Многократное объединение условий"""
complex_condition_reviews = reviews.loc[reviews.country.isin(['Italy', 'France']) & (reviews.points >= 90)]
print(complex_condition_reviews)
print("#"*119)
complex_condition_reviews = reviews.loc[((reviews.country == 'Italy') | (reviews.points >= 90)) & (reviews.price.notnull())]
print(complex_condition_reviews)
print("#"*119)

"""Присваивание данных"""
# Присвоить значение 'everyone' всем значениям в столбце `critic`
reviews['critic'] = 'everyone'

# Создание нового столбца с обратным порядком индексов
reviews['index_backwards'] = range(len(reviews), 0, -1)