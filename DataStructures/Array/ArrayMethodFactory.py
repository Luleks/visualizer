from typing import Callable
from DataStructures.Array.ArrayRules import ArrayRules
from DataStructures.MethodFactory import MethodFactory


class ArrayMethodFactory(MethodFactory):

    def __init__(self, rules: ArrayRules):
        super().__init__(rules)

    def produce(self, method: str) -> Callable:
        if method == 'append':
            return self._rules.append
        elif method == 'bubble':
            return self._rules.bubble_sort
        elif method == 'insertion':
            return self._rules.insertion_sort
        elif method == 'sort':
            return self._rules.sorting_alg
        elif method == 'insert':
            return self._rules.insert_at
        elif method == 'delete':
            return self._rules.delete_at
