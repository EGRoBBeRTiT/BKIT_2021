def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор

    for item in items:
        if len(args) == 1:
            if item.get(args[0]) and item[args[0]] is not None:
                yield item[args[0]]
        else:
            d = {arg : item[arg] for arg in args if item.get(arg) and item[arg] is not None}
            if len(d) != 0:
                yield d



def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in range(len(items)):
            for key, value in items[i].items():
                if key == args[0]:
                    yield value
                    break 
    else:
        for i in range(len(items)):
            dic = dict()
            for key, value in items[i].items():
                if key in args:
                    dic[key] = value
            yield dic


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

if __name__ == '__main__':
    for i in field(goods, 'color'):
        print(i, end=", ")

    for i in field(goods, 'title', 'price', 'color'):
        print(i, end=", ")