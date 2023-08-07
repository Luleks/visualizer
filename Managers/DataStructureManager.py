from abc import abstractmethod
from Managers.UIManager import UIManager

from DataStructures.DataStructureRules import DataStructureRules
from DataStructures.MethodFactory import MethodFactory

from ReusablePygameGUIControls.TextDisplay import TextDisplay
from ReusablePygameGUIControls.CommandButton import CommandButton
from ReusablePygameGUIControls.Colors.ColorConstants import *
from PygameExtensions.Fonts import *

from Commands.RedirectCommand import RedirectCommand
from Commands.RunSettingsCommand import RunSettingsCommand

import os

import pygame


class DataStructureManager(UIManager):
    control_width: int = 120
    control_height: int = 60
    controls_start_y = 100
    left_column_x = 10
    right_column_x = 1070

    def __init__(self, manager_name: str, settings_exe_path: str):
        self._name = manager_name
        self._settings_path = settings_exe_path
        self._rules: DataStructureRules | None = None
        self._method_factory: MethodFactory | None = None

        self.load_rules()

        super().__init__()
        self.__initialize_common_controls()
        self._display_box = TextDisplay(140, 140, 920, 50, GREY, '', WHITE, font25, None)
        self._text_displays.append(self._display_box)

    @abstractmethod
    def pack_rules(self):
        pass

    @abstractmethod
    def load_rules(self):
        pass

    @abstractmethod
    def _load_settings(self):
        pass

    def _navigate_to_settings_file(self):
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        settings_xml = os.path.join(script_dir, 'Settings', self._settings_path, 'bin', 'Debug',
                                    f'{self._settings_path}.xml')
        return settings_xml

    @abstractmethod
    def _init_components(self):
        pass

    def update_statuses(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        super().update_statuses(event, mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._display_box.reset_text()

    def __initialize_common_controls(self):
        return_button = CommandButton(1110, 25, 60, 60, None, '', BLACK, font50, r'Resources/DataStructFolder/back_button.png',
                                      RedirectCommand('main_menu'))

        settings_button = CommandButton(1030, 25, 60, 60, None, '', BLACK, font50,
                                        r'Resources/DataStructFolder/settings_button.png',
                                        RunSettingsCommand(self._settings_path))

        struct_title = TextDisplay(10, 10, 1000, 90, None, self._name, WHITE, font50, None)
        self._actionable.extend([return_button, settings_button])
        self._text_displays.append(struct_title)

    @staticmethod
    def _calculate_gap(number_of_controls: int, number_of_clusters: int):
        total_height = number_of_controls * DataStructureManager.control_height
        leftover_height = 700 - total_height - DataStructureManager.controls_start_y
        gap = leftover_height // (number_of_clusters + 1)
        return gap
