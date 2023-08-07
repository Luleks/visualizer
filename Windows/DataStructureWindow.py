from abc import abstractmethod
from Windows.Window import Window

from ReusablePygameGUIControls.IDrawable import IDrawable

from NonReusablePygameGUI.DataStructureBlock import DataStructureBlock


class DataStructureWindow(Window):

    def __init__(self, background_color: tuple[int, int, int] | None, background_image_path: str | None):
        super().__init__(background_color, background_image_path)
        self._elements: list[DataStructureBlock] = []

    def draw(self, ui_elements: list[IDrawable]) -> None:
        super().draw(ui_elements)

        for block in self._elements:
            block.draw(self._win)

        self._draw_unique_details()

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, new_elements: list):
        self._init_building_blocks(new_elements)

    @abstractmethod
    def _init_building_blocks(self, elements: list):
        pass

    @abstractmethod
    def _draw_unique_details(self):
        pass

    @abstractmethod
    def accept_rules(self, args: tuple):
        pass
