import types

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        
    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        
        nice_list = [y for x in self.list_of_list for y in x] 
        
        if self.cursor >= len(nice_list):
            raise StopIteration
        
        element = nice_list[self.cursor]
        self.cursor += 1
        
        return element

def flat_generator(list_of_lists):
    
    cursor = 0
    nice_list = [y for x in list_of_lists for y in x] 
    
    while True:
        if cursor >= len(nice_list):
            break
        else:
            yield nice_list[cursor]
            cursor += 1
    
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_1()
    test_2()