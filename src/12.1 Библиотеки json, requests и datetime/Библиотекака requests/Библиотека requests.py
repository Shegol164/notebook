import requests

# Например, чтобы получить содержимое страницы по адресу  https://xkcd.com/353/, можно выполнить следующий код:

r = requests.get("https://xkcd.com/353/")
print(r.text)
# r.text— текстовое содержимое ответа;
# r.content— бинарное содержимое ответа, то есть информация в двоичном формате — в виде последовательности нулей и единиц;
# r.json()— JSON-объект, если возможно преобразование ответа в JSON.
print("#" * 119)

# Для отправки POST-запроса необходимо вызвать метод requests.post()
payload = {"my_key": "my_value"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
print("#" * 119)

"""1xx — информационные коды, которые означают, что запрос принят и обрабатывается.
2xx — успешные коды, которые означают, что запрос выполнен успешно.
3xx — перенаправляющие коды, которые означают, что запросу нужно следовать за другим адресом.
4xx — ошибочные коды, которые означают, что запрос содержит ошибку или неверные данные.
5xx — серверные коды, которые означают, что на стороне сервера произошла ошибка при обработке запроса."""

"""При отправке запросов можно ориентироваться на статус-код операции для определения успешности выполнения запросов."""
# Импортируем библиотеку requests
import requests

# Задаем адрес сайта, к которому хотим обратиться
url = "https://example.com"
# Выполняем GET-запрос к сайту и сохраняем ответ в переменную response
response = requests.get(url)
# Получаем статус-код из ответа и выводим его на экран
status_code = response.status_code
print(f"Статус код: {status_code}")
# Проверяем, равен ли статус-код 200, то есть чтобы запрос был успешным
if status_code == 200:
    # Выводим содержимое сайта на экран
    content = response.text
    print(f"Содержимое сайта:\n{content}")
else:
    # Выводим сообщение об ошибке
    print(f"Запрос не был успешным. Возможная причина: {response.reason}")
print(
    "В этом примере: Мы импортируем библиотеку requests.\nЗадаем адрес сайта, к которому хотим обратиться.\nВыполняем GET-запрос к сайту и сохраняем ответ в переменную response\nПолучаем статус-код из ответа и выводим его на экран.\nПроверяем, равен ли статус-код 200, тем самым определяем успешность выполнения запроса. Если статус-код любой неуспешный (не 200), выводим сообщение об ошибке с причиной, которую получаем с помощью response.reason"
)
print("#" * 119)

"""Для получения данных из ответа API в формате JSON с помощью библиотеки 
requests
 можно использовать метод 
response.json().
Код ниже использует библиотеку requests для отправки GET-запроса к API GitHub, чтобы получить список репозиториев пользователя skypro-008.
Затем он фильтрует репозитории, используя только те, которые написаны на языке Python, и выводит их название и ссылку на страницу репозитория."""
import requests

user = "skypro-008"
url = f"https://api.github.com/users/{user}/repos"

response = requests.get(url)

repos = response.json()

for repo in repos:
    if repo["language"] == "Python":
        print(f"Name: {repo['name']}\nLink: {repo['html_url']}\n")
print("#" * 119)

"""Для отправки запроса с параметрами используется параметр  params в методе requests.get:"""
import requests

url = "https://api.apilayer.com/exchangerates_data/convert"

payload = {"amount": "1200", "from": "EUR", "to": "USD"}
headers = {"apikey": "fSHSoKuZ2zVFxstaVw1stEq3GIFqPptc"}

response = requests.get(url, headers=headers, params=payload)

status_code = response.status_code
result = response.json()

print(status_code)
print(result)
print("#" * 119)
