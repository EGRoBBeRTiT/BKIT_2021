# используется для сортировки
from operator import itemgetter
 
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

#одна книга в нескольких магазинах, связь многие-ко-многим
books_shops = [
    BookShop(1,1),
    BookShop(1,2),
    BookShop(2,2),
    BookShop(2,4),
    BookShop(3,3),
    BookShop(3,5),
    BookShop(4,3),
    BookShop(4,1),
    BookShop(5,5),
    BookShop(5,6),
    BookShop(6,6),
    BookShop(6,2),
    BookShop(7,4),
    BookShop(7,5),
    BookShop(8,4),
    BookShop(8,1),
    BookShop(9,6),
    BookShop(10,1),
    BookShop(10,4),
    BookShop(10,5),
]
 
def main():
    """Основная функция"""
    # Соединение данных один-ко-многим 
    one_to_many_1 = [(b.name, b.price, s.name) 
        for s in shops 
        for b in books 
        if b.shop_id==s.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(s.name, ed.shop_id, ed.book_id) 
        for s in shops 
        for ed in books_shops 
        if s.id==ed.shop_id]
    
    many_to_many = [(b.name, b.price, shop_name) 
        for shop_name, shop_id, book_id in many_to_many_temp
        for b in books if b.id==book_id]

    #Нужно вывести список книг, названия которых заканчивается на "а", и названия их магазинов
    print('Задание Д1')
    res_11 = []
    # Перебираем все магазины
    for s in shops:
        # Список книг магазина
        s_books = list(filter(lambda i: i[2]==s.name, one_to_many_1))  
        # Если магазин не пустой        
        if len(s_books) > 0:
            for i in range(len(s_books)):
                if s_books[i][0][-1] == 'а':
                    res_11.append((s_books[i][0], s.name))
    print(res_11)

    #нужно вывести список магазинов со средней стоимостью книг
    print('\nЗадание Д2')
    res_12_unsorted = []
    # Перебираем все магазины
    for s in shops:
        # Список книг в магазине
        s_books = list(filter(lambda i: i[2]==s.name, one_to_many_1))
        # Если магазин не пустой        
        if len(s_books) > 0:
            # Стоимость книг в магазине
            s_prices = [price for _,price,_ in s_books]
            # Суммарная стоимость книг в магазине
            s_prices_sum = sum(s_prices)
            #Средняя стоимость книг в магазине
            av_prices = s_prices_sum/len(s_prices)
            res_12_unsorted.append((s.name, av_prices))
 
    # Сортировка по средней стоимости
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    #Нужно вывести все магазины, в названии которых есть слово "книги", и список продаваемых в них книг
    print('\nЗадание Д3')
    res_13 = {}
    # Перебираем все магазины
    for s in shops:
        if ('книги' in s.name):
            # Список книг магазина
            s_books = list(filter(lambda i: i[2]==s.name, many_to_many))
            # Только название книг
            s_books_names = [x for x,_,_ in s_books]
            # Добавляем результат в словарь
            # ключ - магазин, значение - список названий книг
            res_13[s.name] = s_books_names
 
    print(res_13)

if __name__ == '__main__':
    main()
