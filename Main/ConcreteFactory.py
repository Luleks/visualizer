from Main.AbstractFactory import AbstractFactory

from Managers.UIManager import UIManager
from Windows.Window import Window
from Synchronizers.Synchronizer import Synchronizer

from Managers.MainMenuManager import MainMenuManager
from Windows.MainMenuWindow import MainMenuWindow

from Managers.ArrayManager import ArrayManager
from Windows.ArrayWindow import ArrayWindow


class ConcreteFactory(AbstractFactory):

    def produce(self, module: str = None) -> tuple[UIManager, Window, Synchronizer | None]:
        if module is None or module == 'str':
            manager = MainMenuManager()
            window = MainMenuWindow(None, r'Resources/main_menu_folder/main_menu_background.jpg')
            return manager, window, None
        elif module == 'array':
            manager = ArrayManager()
            window = ArrayWindow(None, r'Resources/DataStructFolder/data_struct_background.jpg')
            synchronizer = Synchronizer(window, manager)
            return manager, window, synchronizer
        return MainMenuManager(), MainMenuWindow(None, r'Resources/main_menu_folder/main_menu_background.jpg'), None
