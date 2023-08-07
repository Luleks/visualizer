from typing import Callable
from DataStructures.Array.ArrayRules import ArrayRules
from DataStructures.MethodFactory import MethodFactory


class ArrayMethodFactory(MethodFactory):

    def produce(self, method: str, rules: ArrayRules) -> Callable:
        if method == 'append':
            return rules.append
        elif method == 'bubble':
            return rules.bubble_sort
        elif method == 'insertion':
            return rules.insertion_sort
        elif method == 'sort':
            return rules.sorting_alg
        elif method == 'insert':
            return rules.insert_at
        elif method == 'delete':
            return rules.delete_at
