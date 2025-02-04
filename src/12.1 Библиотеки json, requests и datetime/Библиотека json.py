import json

#Метод loads()— используется для преобразования строки JSON в объект Python.
data = '{"name": "John Smith", "age": 30, "city": "New York"}'
parsed_data = json.loads(data)
print(parsed_data["name"])
print(type(parsed_data))
print("#"*119)

#Метод dumps()— используется для преобразования объекта Python в строку JSON.
data = {
    "name": "John Smith",
    "age": 30,
    "city": "New York"
}
# json_data - строка, тип str
json_data = json.dumps(data)
print(json_data)
print(type(json_data))
print("#"*119)

#Метод load — загружает данные из файла в формате JSON и преобразует их в объект Python.
with open('data.json') as f:
    data = json.load(f)

print(data) # data - словарь, тип dict
print("#"*119)

#Метод dump — преобразует объект Python в формат JSON и записывает его в файл
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
with open('output.json', 'w') as f:
    json.dump(data, f)
 # Задача

book_info ={"title" : "Sherlock Holmes", "author" : "Artur Conan Doyle", "publication_year" : 1887, "genres" : ["detective", "novel"]}
book_info_str = json.dumps(book_info)
print(book_info_str)
print("#"*119)

book_info_str = '{"title": "Sherlock Holmes", "author": "Artur Conan Doyle", "publication_year": 1887, "genres": ["detective", "novel"]}'
book_info = json.loads(book_info_str)
print(book_info)
print(type(book_info))
print("#"*119)

with open('data_1.json',  'w') as json_file:
    json.dump(book_info, json_file)

with open('data_1.json') as json_file:
    book_info = json.load(json_file)
print(book_info)
