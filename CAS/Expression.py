class Expr():
    @property
    def QssType(self):
        return self.__QssTypeList


class Symbol(Expr):
    def __init__(self, name:str, QssTypeList:list = []):
        self.__QssTypeList = QssTypeList
        self.__name = name

    def __str__(self):
        return f'\033[4;33m{self.__name}\033[0m'
            

class Expression(Expr):
    def __init__(self, operator, *items):
        self.operator = operator
        self.item = items
    @property
    def operator_type(self):
        return self.operator.__class__
    def __str__(self):
        return self.operator._output_form(self.__item)


if __name__ == '__main__':
    a = Symbol('a')
    print(a)
