from Windows.DataStructureWindow import DataStructureWindow
import pygame
from ReusablePygameGUIControls.Colors.ColorConstants import *
from NonReusablePygameGUI.ArrayBlock import ArrayBlock


class ArrayWindow(DataStructureWindow):

    def __init__(self, background_color: tuple[int, int, int] | None, background_image_path: str | None):
        super().__init__(background_color, background_image_path)
        self.__array_size = None
        self.__block_size = None
        self.__start_x = None
        self.__start_y = None
        self.__additional_lines_x = None

    def accept_rules(self, args: tuple):
        self.__array_size = args[0]
        self.calculate_drawing_parameters()
        self.elements = args[1]
        if self._elements:
            self.__additional_lines_x = self._elements[-1].x + self.__block_size
        else:
            self.__additional_lines_x = self.__start_x

    def calculate_drawing_parameters(self):
        start_block_side = 100

        while start_block_side * self.__array_size > DataStructureWindow.workspace_width - 20:
            start_block_side -= 2
        start_x = DataStructureWindow.workspace_x + (DataStructureWindow.workspace_width - 20 - start_block_side *
                                                     self.__array_size) // 2
        start_y = DataStructureWindow.workspace_y + (DataStructureWindow.workspace_height - start_block_side) // 2

        self.__block_size = start_block_side
        self.__start_x = start_x
        self.__start_y = start_y

        if self._elements:
            self.__additional_lines_x = self._elements[-1].x + self.__block_size
        else:
            self.__additional_lines_x = self.__start_x

    def _init_building_blocks(self, elements: list):
        self._elements.clear()
        for i, block_val in enumerate(elements):
            self._elements.append(ArrayBlock(self.__start_x + i * self.__block_size, self.__start_y,
                                             self.__block_size, self.__block_size, block_val))

    def _draw_unique_details(self):
        pygame.draw.line(self._win, BLACK, (DataStructureWindow.workspace_x, self.__start_y),
                         (DataStructureWindow.workspace_x + DataStructureWindow.workspace_width, self.__start_y), 3)
        pygame.draw.line(self._win, BLACK, (DataStructureWindow.workspace_x, self.__start_y + self.__block_size - 1),
                         (DataStructureWindow.workspace_x + DataStructureWindow.workspace_width,
                          self.__start_y + self.__block_size - 1), 3)

        for i in range(self.__array_size - len(self._elements) + 1):
            pygame.draw.line(self._win, BLACK, (self.__additional_lines_x + self.__block_size * i, self.__start_y),
                             (self.__additional_lines_x + self.__block_size * i, self.__start_y + self.__block_size), 3)

    def animation(self, instruction: dict):
        if elements := instruction.get('elements'):
            self._init_building_blocks(elements)
            self.calculate_drawing_parameters()
