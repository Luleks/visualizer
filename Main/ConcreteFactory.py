from Main.AbstractFactory import AbstractFactory

from Managers.UIManager import UIManager
from Windows.Window import Window

from Managers.MainMenuManager import MainMenuManager
from Windows.MainMenuWindow import MainMenuWindow


class ConcreteFactory(AbstractFactory):

    def produce(self, module: str = None) -> tuple[UIManager, Window]:
        if module is None or module == 'str':
            return MainMenuManager(), MainMenuWindow(None, r'Resources/main_menu_folder/main_menu_background.jpg')
        return MainMenuManager(), MainMenuWindow(None, r'Resources/main_menu_folder/main_menu_background.jpg')
