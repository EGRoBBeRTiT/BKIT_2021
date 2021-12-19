import unittest
from RK1 import RK1
from ds import books, shops, books_shops

res_1 = [
    ('Дракула', 'Азбука'),
    ('Анна Каренина', 'Книжный бум'),
    ('Дюна', 'Мир книги')
]


res_2 = [
    ('Азбука', 680.0),
    ('Букварики', 670.0),
    ('Дом книги', 550.0),
    ('Книжный бум', 530.0),
    ('Мир книги', 530.0),
    ('Литера', 500.0)
]

res_3 = {
    'Дом книги':
        [
            'Война и мир',
            'Унесённые ветром'
        ],
    'Мир книги':
        [
            'Остров сокровищ',
            'Дюна',
            'Повелитель мух'
        ]
}


class MyTestCase(unittest.TestCase):
    def test_N1(self):
        rk = RK1(shops, books, books_shops)
        self.assertEqual(res_1, rk.N1())

    def test_N2(self):
        rk = RK1(shops, books, books_shops)
        self.assertEqual(res_2, rk.N2())

    def test_N3(self):
        rk = RK1(shops, books, books_shops)
        self.assertEqual(res_3, rk.N3())

if __name__ == '__main__':
    unittest.main()
