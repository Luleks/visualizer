from DataStructures.Array.ArrayRules import ArrayRules


class StaticArrayRules(ArrayRules):

    def __init__(self):
        super().__init__(4)
        self._elements = []
        self.sorting_alg = self.bubble_sort

    def append(self, new_element: int) -> None:
        if self._size == len(self._elements):
            raise IndexError("Static array overflow")
        self._elements.append(new_element)
        yield {'elements': self._elements}
        yield {'end': True}

    def insert_at(self, index: int, value: int):
        if index > len(self._elements) or index < 0:
            raise IndexError("List index out of range")
        if self._size == len(self._elements):
            raise IndexError("Static array overflow")
        self._elements.append(0)
        for i in range(len(self._elements)-1, index, -1):
            self._elements[i] = self._elements[i - 1]
            yield {'elements': self._elements}
        self._elements[index] = value
