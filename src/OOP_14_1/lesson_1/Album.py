"""
Создай класс Album у которого есть поля

- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - это **список**

**Создай два экземпляра album_1 и album_2**

Исполнитель: Queen

Название: Killer Queen

Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica

Название: Black Album

Треки: Enter Sandman, Sad But True, Holier Than Thou
"""


class Album:
    def __init__(self, artist, title, tracks):
        self.artist = artist
        self.title = title
        self.tracks = tracks
