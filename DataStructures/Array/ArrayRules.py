from DataStructures.DataStructureRules import DataStructureRules
from abc import abstractmethod


class ArrayRules(DataStructureRules):
    def __init__(self, size: int):
        self._elements = []
        self._size = size
        self._sorting_alg = None

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        if new_size <= 0:
            raise ValueError("Array size must be positive integer")
        self._size = new_size

    @property
    def elements(self) -> list[int]:
        return self._elements

    @elements.setter
    def elements(self, value) -> None:
        self._elements = value

    @property
    def sorting_alg(self):
        return self._sorting_alg

    @sorting_alg.setter
    def sorting_alg(self, value: str):
        if value == 'Bubble':
            self._sorting_alg = self.bubble_sort
        elif value == 'Selection':
            self._sorting_alg = self.selection_sort
        else:
            self._sorting_alg = self.insertion_sort

    @abstractmethod
    def append(self, new_element: int) -> None:
        pass

    @abstractmethod
    def insert_at(self, index: int, value: int):
        pass

    def delete_at(self, index: int):
        if index >= len(self._elements) or index < 0:
            raise IndexError("List index out of range")

        deleted_element: int = self._elements[index]
        for i in range(index, len(self._elements) - 1):
            self._elements[i] = self._elements[i + 1]
            yield {'elements': self._elements}
        self._elements.pop()

        yield {'end': f'Deleted element: {deleted_element}'}

    def linear_search(self, value: int):
        i: int = 0
        while i < len(self._elements) and self._elements[i] != value:
            yield {'index': [i]}
            i += 1
        if i == len(self._elements):
            yield {'index': [-1]}
            yield {'end': f'Element {value} not found'}
        else:
            yield {'index': [i]}
            yield {'end': f'Element {value} found at index {i}'}

    def binary_search(self, value: int):
        if not self._elements:
            yield {'index': [-1]}
        else:
            lower_index = 0
            higher_index = len(self._elements) - 1
            middle = (lower_index + higher_index) // 2
            yield {'index': [lower_index, middle, higher_index]}

            while lower_index <= higher_index and self._elements[middle] != value:
                if self._elements[middle] > value:
                    higher_index = middle - 1
                else:
                    lower_index = middle + 1
                middle = (lower_index + higher_index) // 2
                yield {'index': [lower_index, middle, higher_index]}

            if self._elements[middle] == value:
                yield {'index': [middle]}
                yield {'end': f'Element {value} found at index {middle}'}
            else:
                yield {'index': [-1]}
                yield {'end': f'Element {value} not fount'}

    def bubble_sort(self):
        for i in range(len(self._elements) - 1, 0, -1):
            for j in range(0, i):
                yield {'index': [j, j+1]}
                if self._elements[j] >= self._elements[j + 1]:
                    self._elements[j], self._elements[j + 1] = self._elements[j + 1], self._elements[j]
                    yield {'elements': self._elements}
        yield {'end': 'Et voila'}

    def selection_sort(self):
        for i in range(len(self._elements) - 1):
            i_min = i
            for j in range(i + 1, len(self._elements)):
                yield {'index': [i, j, i_min]}
                if self._elements[j] < self._elements[i_min]:
                    i_min = j

            self._elements[i], self._elements[i_min] = self._elements[i_min], self._elements[i]
            yield {'elements': self._elements}
        yield {'end': 'Et voila'}

    def insertion_sort(self):
        for i in range(1, len(self._elements)):
            temp = self._elements[i]
            j = i - 1
            while j >= 0 and self._elements[j] > temp:
                yield {'index': [i, j]}
                self._elements[j + 1] = self._elements[j]
                j -= 1
                yield {'elements': self._elements}
            self._elements[j + 1] = temp
            yield {'elements': self._elements}
        yield {'end': 'Et voila'}

    def __repr__(self):
        return f'{self.__class__.__name__} {self.size} {self.sorting_alg}'
