class Book:
    def __init__(self, author, title, publisher, year, page_count):
        self._author = author
        self._title = title
        self._publisher = publisher
        self._year = year
        self._page_count = page_count
    @property
    def title(self):
        return self._title
    @property
    def publisher(self):
        return self._publisher
    def __str__(self):
        return (f"Book: {self._title}, Author: {self._author}, Publisher: {self._publisher},"
                f"Year: {self._year}, Page Count: {self._page_count}")
# Создаем экземпляр класса Book
book1 = Book("Джон Р. Р Толкин", "Властелин колец: Хранители кольца.", "Астрель", 2011, 563)
# Получаем доступ к свойству "Название" (title) и выводим его на экран
print(book1.title)  # Выведет: "Властелин колец: Хранители кольца."
# Получаем доступ к свойству "Издательство" (publisher) и выводим его на экран
print(book1.publisher)  # Выведет: "Астрель"
# Выводим информацию о книге с помощью метода __str__
print(book1)  # Выведет: "Book: Властелин колец: Хранители кольца., Author: Джон Р. Р Толкин , Publisher: Астрель, Year: 2011, Page Count: 563"