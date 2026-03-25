class Book:
    """Базовый класс книги"""
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__is_borrowed = False  # приватный атрибут
    
    def borrow(self):
        """Взять книгу"""
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False
    
    def return_book(self):
        """Вернуть книгу"""
        self.__is_borrowed = False
    
    def get_info(self):
        """Получить информацию о книге"""
        status = "Выдана" if self.__is_borrowed else "Доступна"
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {status}"
    
    def is_borrowed(self):
        """Получить статус книги (для доступа из наследников)"""
        return self.__is_borrowed


class EBook(Book):
    """Класс электронной книги"""
    
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size  # размер файла в МБ
    
    def borrow(self):
        """Взять электронную книгу (всегда доступна)"""
        # Для электронной книги вызываем родительский метод borrow,
        # но он всегда будет возвращать True, так как логика аренды файла
        # позволяет неограниченное количество копий
        if not self.is_borrowed():
            return super().borrow()
        else:
            # Даже если уже взята, всё равно возвращаем True (неограниченный тираж)
            return True
    
    def get_info(self):
        """Получить информацию об электронной книге"""
        base_info = super().get_info()
        return f"{base_info}, Размер файла: {self.file_size} МБ"


class AudioBook(Book):
    """Класс аудиокниги"""
    
    def __init__(self, title, author, year, duration, narrator):
        super().__init__(title, author, year)
        self.duration = duration  # длительность в минутах
        self.narrator = narrator  # имя чтеца
    
    def get_info(self):
        """Получить информацию об аудиокниге"""
        base_info = super().get_info()
        return f"{base_info}, Чтец: {self.narrator}, Длительность: {self.duration} мин"
    
    def __str__(self):
        """Краткая информация при print()"""
        return f"Аудиокнига: {self.title} - {self.narrator}"


# Пример использования
if __name__ == "__main__":
    # Проверка базового класса Book
    book1 = Book("Война и мир", "Лев Толстой", 1869)
    print(book1.get_info())
    print(book1.borrow())  # True
    print(book1.get_info())
    print(book1.borrow())  # False
    book1.return_book()
    print(book1.get_info())
    print("-" * 50)
    
    # Проверка EBook
    ebook = EBook("Цифровая книга", "Автор", 2024, 2.5)
    print(ebook.get_info())
    print(ebook.borrow())  # True
    print(ebook.get_info())
    print(ebook.borrow())  # True (всегда доступна)
    print("-" * 50)
    
    # Проверка AudioBook
    audiobook = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 720, "Иван Иванов")
    print(audiobook.get_info())
    print(audiobook.borrow())  # True
    print(audiobook)  # Вызов __str__
    print(audiobook.get_info())