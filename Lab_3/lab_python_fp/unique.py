
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        ignore_case = kwargs.get('ignore_case', False)
        data = []
        for item in items:
            if isinstance(item, str) and not ignore_case:
                data1 = list(map(lambda x: x.lower(), data))
                if item.lower() not in data1:
                    data.append(item)
            elif item not in data:
                data.append(item)
        self.data = data
        self.index = 0



    def __next__(self):
        array_length = len(self.data)
        prev_index = self.index

        if self.index < array_length:
            self.index += 1

        if prev_index <= array_length and prev_index < array_length:
            return self.data[prev_index]
        else:
            self.index = 0
            raise StopIteration


    def __iter__(self):
        return self
