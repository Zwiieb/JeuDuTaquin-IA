class Node:

    def __init__(self, _value):
        self.__value = _value
        self.__parent = None
        self.__left = None
        self.__right = None

    # getter / setter
    if 1:
        @property
        def _value(self):
            return self.__value

        @_value.setter
        def _value(self, _x):
            self.__value = _x

        @property
        def _parent(self):
            return self.__parent

        @_parent.setter
        def _parent(self, _x):
            self.__parent = _x

        @property
        def _left(self):
            return self.__left

        @_left.setter
        def _left(self, _x):
            self.__left = _x

        @property
        def _right(self):
            return self.__right

        @_right.setter
        def _right(self, _x):
            self.__right = _x


class Tree:

    def __init__(self, _value):
        self.__root = Node(_value)

    # méthodes
    def insert(self, _val, trace):
        if trace == 1:
            print("_val:", _val)
            print("__value", self.__root._value(), "\n")

        if _val < self.__root._value():
            if self.__root._left() is None:
                self.__root._left(Node(_val))
                self.__root._left().__parent = self.__root
            else:
                Tree.insert(self.__root._left(), _val, trace)
        elif self.__root._value() < _val:
            if self.__root._right() is None:
                self.__root._right(Node(_val))
                self.__root._right().__parent = self.__root
            else:
                Tree.insert(self.__root._right, _val, trace)


liste = [8, 4, 3, 2, 9, 1, 2]
tree = Tree(liste[0])
for i in range(1, len(liste)):
    tree.insert(liste[i], 0)
