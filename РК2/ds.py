class Book:
    """Книга"""

    def __init__(self, id, name, price, shop_id):
        self.id = id
        self.name = name
        self.price = price
        self.shop_id = shop_id


class Shop:
    """Книжный магазин"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookShop:
    """
    'Книги книжного магазина' для реализации
    связи многие-ко-многим
    """

    def __init__(self, book_id, shop_id):
        self.book_id = book_id
        self.shop_id = shop_id


# Магазины (ID, название)
shops = [
    Shop(1, 'Азбука'),
    Shop(2, 'Букварики'),
    Shop(3, 'Дом книги'),
    Shop(4, 'Книжный бум'),
    Shop(5, 'Литера'),
    Shop(6, 'Мир книги'),
]

# Книги (ID, название, стоимость, ID магазина)
books = [
    Book(1, 'Властелин колец', 760, 1),
    Book(2, 'Гарри Поттер', 670, 2),
    Book(3, 'Война и мир', 550, 3),
    Book(4, 'Унесённые ветром', 550, 3),
    Book(5, 'Остров сокровищ', 500, 5),
    Book(6, 'Дюна', 560, 6),
    Book(7, 'Граф Монте-Кристо', 610, 4),
    Book(8, 'Анна Каренина', 450, 4),
    Book(9, 'Повелитель мух', 500, 6),
    Book(10, 'Дракула', 600, 1),
]

# одна книга в нескольких магазинах, связь многие-ко-многим
books_shops = [
    BookShop(1, 1),
    BookShop(1, 2),
    BookShop(2, 2),
    BookShop(2, 4),
    BookShop(3, 3),
    BookShop(3, 5),
    BookShop(4, 3),
    BookShop(4, 1),
    BookShop(5, 5),
    BookShop(5, 6),
    BookShop(6, 6),
    BookShop(6, 2),
    BookShop(7, 4),
    BookShop(7, 5),
    BookShop(8, 4),
    BookShop(8, 1),
    BookShop(9, 6),
    BookShop(10, 1),
    BookShop(10, 4),
    BookShop(10, 5),
]