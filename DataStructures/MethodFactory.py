from abc import ABC, abstractmethod
from typing import Callable
from DataStructures.DataStructureRules import DataStructureRules


class MethodFactory(ABC):

    def __init__(self, rules: DataStructureRules):
        self._rules = rules

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, new_rules: DataStructureRules):
        self._rules = new_rules

    @abstractmethod
    def produce(self, method: str) -> Callable:
        pass
