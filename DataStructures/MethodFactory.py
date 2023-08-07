from abc import ABC, abstractmethod
from typing import Callable
from DataStructures.DataStructureRules import DataStructureRules


class MethodFactory(ABC):

    def __init__(self, rules: DataStructureRules):
        self.__rules = rules

    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, new_rules: DataStructureRules):
        self.__rules = new_rules

    @abstractmethod
    def produce(self, method: str) -> Callable:
        pass
