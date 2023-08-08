from Managers.DataStructureManager import DataStructureManager

from PygameExtensions.Fonts import *

from NonReusablePygameGUI.CallableButton import CallableButton
from ReusablePygameGUIControls.InputForm import InputForm
from ReusablePygameGUIControls.TextDisplay import TextDisplay
from ReusablePygameGUIControls.Colors.ColorConstants import *

from DataStructures.Array.ArrayMethodFactory import ArrayMethodFactory
from DataStructures.Array.DynamicArrayRules import DynamicArrayRules
from DataStructures.Array.StaticArrayRules import StaticArrayRules

import xml.etree.ElementTree as ET


class ArrayManager(DataStructureManager):

    def __init__(self):
        super().__init__('Array', r'ArraySettings')

    def _get_factory(self) -> ArrayMethodFactory:
        return ArrayMethodFactory(self._rules)

    def _init_components(self):
        #  Creating left column of controls
        left_gap = DataStructureManager._calculate_gap(8, 3)
        start_y = DataStructureManager.controls_start_y + left_gap

        input_insert = InputForm(DataStructureManager.left_column_x,
                                 start_y + DataStructureManager.control_height,
                                 DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                 'Enter value', BLACK, font20, None, 3)
        button_insert = CallableButton(DataStructureManager.left_column_x, start_y, DataStructureManager.control_width,
                                       DataStructureManager.control_height, GREY, 'Insert', BLACK, font25, None,
                                       'append', self._method_factory, [input_insert], int)
        input_insert_at_index = InputForm(DataStructureManager.left_column_x,
                                          start_y + DataStructureManager.control_height * 3 + left_gap,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Enter index', BLACK, font20, None, 3)
        input_insert_at_value = InputForm(DataStructureManager.left_column_x,
                                          start_y + DataStructureManager.control_height * 4 + left_gap,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Enter value', BLACK, font20, None, 3)
        button_insert_at = CallableButton(DataStructureManager.left_column_x,
                                          start_y + 2 * DataStructureManager.control_height + left_gap,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Insert at', BLACK, font25, None, 'insert',
                                          self._method_factory, [input_insert_at_index, input_insert_at_value], int)
        input_delete_at_index = InputForm(DataStructureManager.left_column_x,
                                          start_y + DataStructureManager.control_height * 6 + left_gap * 2,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Enter index', BLACK, font20, None, 3)
        display_delete_returned = TextDisplay(DataStructureManager.left_column_x,
                                              start_y + DataStructureManager.control_height * 7 + left_gap * 2,
                                              DataStructureManager.control_width, DataStructureManager.control_height,
                                              GREY, 'Deleted: ', BLACK, font20, None)
        button_delete_at = CallableButton(DataStructureManager.left_column_x,
                                          start_y + DataStructureManager.control_height * 5 + left_gap * 2,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Delete at', BLACK, font25, None, 'delete',
                                          self._method_factory, [input_delete_at_index], int)

        #  Creating right column of controls
        right_gap = DataStructureManager._calculate_gap(7, 3)
        start_y = DataStructureManager.controls_start_y + right_gap
        input_lin_search_val = InputForm(DataStructureManager.right_column_x,
                                         start_y + DataStructureManager.control_height,
                                         DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                         'Enter value', BLACK, font20, None, 3)
        display_lin_search_returned = TextDisplay(DataStructureManager.right_column_x,
                                                  start_y + DataStructureManager.control_height * 2,
                                                  DataStructureManager.control_width, DataStructureManager.control_height,
                                                  GREY, 'At index: ', BLACK, font20, None)
        button_lin_search = CallableButton(DataStructureManager.right_column_x, start_y, DataStructureManager.control_width,
                                           DataStructureManager.control_height, GREY, 'Linear search', BLACK, font18,
                                           None, 'linear', self._method_factory,
                                           [input_lin_search_val], int)
        input_bin_search_val = InputForm(DataStructureManager.right_column_x,
                                         start_y + DataStructureManager.control_height * 4 + right_gap,
                                         DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                         'Enter value', BLACK, font20, None, 3)
        display_bin_search_returned = TextDisplay(DataStructureManager.right_column_x,
                                                  start_y + DataStructureManager.control_height * 5 + right_gap,
                                                  DataStructureManager.control_width, DataStructureManager.control_height,
                                                  GREY, 'At index: ', BLACK, font20, None)
        button_bin_search = CallableButton(DataStructureManager.right_column_x,
                                           start_y + DataStructureManager.control_height * 3 + right_gap,
                                           DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                           'Binary search', BLACK, font18, None, 'binary',
                                           self._method_factory, [input_bin_search_val], int)

        button_sort = CallableButton(DataStructureManager.right_column_x,
                                     start_y + DataStructureManager.control_height * 6 + right_gap * 2,
                                     DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                     'Sort', BLACK, font20, None, 'sort',
                                     self._method_factory, [], None)
        self._actionable.extend([button_insert, input_insert, button_insert_at, input_insert_at_index,
                                 input_insert_at_value, button_delete_at, input_delete_at_index, button_lin_search,
                                 input_lin_search_val, button_bin_search, input_bin_search_val, button_sort])
        self._text_displays.extend([display_delete_returned, display_lin_search_returned, display_bin_search_returned])

    def pack_rules(self):
        return self._rules.size, self._rules.elements

    def load_rules(self):
        array_type, array_size, sorting_alg = self._load_settings()

        if array_type == 'Static':
            new_rules = StaticArrayRules()
        else:
            new_rules = DynamicArrayRules()
        new_rules.size = int(array_size)
        new_rules.sorting_alg = sorting_alg

        if self._rules is not None:
            new_rules.elements = self._rules.elements

        if new_rules.size < len(new_rules.elements):
            new_rules.size = len(new_rules.elements)

        self._rules = new_rules

    def _load_settings(self):
        settings_file = self._navigate_to_settings_file()
        tree = ET.parse(settings_file)

        array_type = tree.find('array_type').text
        array_size = tree.find('array_size').text
        sorting_alg = tree.find('sorting_alg').text

        return array_type, array_size, sorting_alg
