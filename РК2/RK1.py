
# используется для сортировки
from operator import itemgetter
from ds import shops, books, books_shops

class RK1:
    def __init__(self, shops, books, books_shops):
        self.shops = shops
        self.books = books
        self.books_shops = books_shops

        # Соединение данных один-ко-многим
        self.one_to_many_1 = [(b.name, b.price, s.name)
                         for s in shops
                         for b in books
                         if b.shop_id == s.id]

        # Соединение данных многие-ко-многим
        self.many_to_many_temp = [(s.name, ed.shop_id, ed.book_id)
                             for s in shops
                             for ed in books_shops
                             if s.id == ed.shop_id]

        self.many_to_many = [(b.name, b.price, shop_name)
                        for shop_name, shop_id, book_id in self.many_to_many_temp
                        for b in books if b.id == book_id]


    def N1(self):
        print('Задание Д1')
        res_11 = []
        # Перебираем все магазины
        for s in shops:
            # Список книг магазина
            s_books = list(filter(lambda i: i[2] == s.name, self.one_to_many_1))
            # Если магазин не пустой
            if len(s_books) > 0:
                for i in range(len(s_books)):
                    if s_books[i][0][-1] == 'а':
                        res_11.append((s_books[i][0], s.name))
        print(res_11)
        return res_11


    def N2(self):
        #нужно вывести список магазинов со средней стоимостью книг
        print('\nЗадание Д2')
        res_12_unsorted = []
        # Перебираем все магазины
        for s in shops:
            # Список книг в магазине
            s_books = list(filter(lambda i: i[2]==s.name, self.one_to_many_1))
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
        return res_12


    def N3(self):
        #Нужно вывести все магазины, в названии которых есть слово "книги", и список продаваемых в них книг
        print('\nЗадание Д3')
        res_13 = {}
        # Перебираем все магазины
        for s in shops:
            if ('книги' in s.name):
                # Список книг магазина
                s_books = list(filter(lambda i: i[2]==s.name, self.many_to_many))
                # Только название книг
                s_books_names = [x for x,_,_ in s_books]
                # Добавляем результат в словарь
                # ключ - магазин, значение - список названий книг
                res_13[s.name] = s_books_names

        print(res_13)
        return res_13


if __name__ == '__main__':
    rk1 = RK1(shops, books, books_shops)
    rk1.N1()
    rk1.N2()
    rk1.N3()