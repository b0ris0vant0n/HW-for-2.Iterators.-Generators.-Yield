nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

any_nested_list = [
    0,
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[[1, 2], None],
]

# 1. Написать итератор, который принимает список списков, и возвращает их плоское представление
class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_
        self.len_list = len(self.list_)
        self.cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.nested_coursor = 0
        return self

    def __next__(self):
        if self.nested_coursor == len(self.list_[self.cursor]):
            iter(self)
        if self.cursor == self.len_list:
            raise StopIteration
        self.nested_coursor += 1
        return self.list_[self.cursor][self.nested_coursor - 1]

# 2. Написать генератор, который принимает список списков, и возвращает их плоское представление.
def flat_generator(list_):
    for item in list_:
        for nested_item in item:
            yield nested_item

# 3.* Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности
class FlatIterator2:
    def __init__(self, list_):
        self.list_ = list_
        self.start = -1
        self.end = len(self.list_)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        while self.start < self.end:
            if type(self.list_[self.start]) is not list:
                return self.list_[self.start]
            else:
                for x in FlatIterator2(self.list_[self.start]):
                    return x

        if self.start == self.end:
            raise StopIteration

# 4.* Написать генератор аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности
def flat_any_list(list_):
    flatlist = []
    for item in list_:
        if type(item) is list:
            flatlist += flat_any_list(item)
        else:
            flatlist += [item]
    return flatlist


if __name__ == '__main__':
    print(' Задание №1')
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print('\n Задание №2')
    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)

    print('\n Задание №3')
    for item in any_nested_list:
        if type(item) is list:
            for x in FlatIterator2(item):
                print(x)
        else:
            print(item)

    print('\n Задание №4')
    for item in flat_any_list(any_nested_list):
        print(item)


