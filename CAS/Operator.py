from Expression import *

# try not create container
class OrderedList(list):
    def __init__(self, key = lambda x: x):
        self._container = []
        self._key = key
    def __ordered_add(self, add_item):
        #if empty
        if not self._container:
            self._container.append([add_item])
            return
        for index, item in enumerate(self._container):
            if self._key(item[0]) == self._key(add_item):
                item.append(add_item)
                return
            elif self._key(item[0]) > self._key(add_item):
                self._container.insert(index, [add_item])
                return
        self._container.append([add_item])
    def append(self, *args):
        if not args:
            return self
        for add_item in args:
            self.__ordered_add(add_item)
    def flatten(self):
        temp = []
        for i in self._container:
            temp += i
        return temp
    def __str__(self):
        return self.flatten().__str__()
    def __repr__(self):
        return self.flatten().__repr__()


class Operator(Expression):
    def __init__(self) -> Expression:
        self.item = OrderList()
    def __init__(self, a:Expr, b:Expr, *items) -> Expression:
        self.item = 1 
    def add(self, item):
        pass



if __name__ == '__main__':
    a = OrderedList()
    a.append(2)
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(1)
    a.append(3)
