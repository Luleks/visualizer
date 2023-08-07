from abc import ABC, abstractmethod
from typing import Callable
from DataStructures.DataStructureRules import DataStructureRules


class MethodFactory(ABC):

    @abstractmethod
    def produce(self, method: str, rules: DataStructureRules) -> Callable:
        pass
