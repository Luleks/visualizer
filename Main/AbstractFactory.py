from Managers.UIManager import UIManager
from Windows.Window import Window
from Synchronizers.Synchronizer import Synchronizer
from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def produce(self, module: str = None) -> tuple[UIManager, Window, Synchronizer | None]:
        pass
