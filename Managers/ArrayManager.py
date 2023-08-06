from Managers.DataStructureManager import DataStructureManager

from PygameExtensions.Fonts import *

from ReusablePygameGUIControls.Button import Button
from ReusablePygameGUIControls.InputForm import InputForm
from ReusablePygameGUIControls.TextDisplay import TextDisplay
from ReusablePygameGUIControls.Colors.ColorConstants import *


class ArrayManager(DataStructureManager):

    def __init__(self):
        super().__init__('Array', r'ArraySettings')

    def _init_components(self):
        #  Creating left column of controls
        left_gap = DataStructureManager._calculate_gap(8, 3)
        start_y = DataStructureManager.controls_start_y + left_gap

        button_insert = Button(DataStructureManager.left_column_x, start_y, DataStructureManager.control_width,
                               DataStructureManager.control_height, GREY, 'Insert', BLACK, font25, None, None)
        input_insert = InputForm(DataStructureManager.left_column_x,
                                 start_y + DataStructureManager.control_height,
                                 DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                 'Enter value', BLACK, font20, None, 3)
        button_insert_at = Button(DataStructureManager.left_column_x,
                                  start_y + 2 * DataStructureManager.control_height + left_gap,
                                  DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                  'Insert at', BLACK, font25, None, None)
        input_insert_at_index = InputForm(DataStructureManager.left_column_x,
                                          start_y + DataStructureManager.control_height * 3 + left_gap,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Enter index', BLACK, font20, None, 3)
        input_insert_at_value = InputForm(DataStructureManager.left_column_x,
                                          start_y + DataStructureManager.control_height * 4 + left_gap,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Enter value', BLACK, font20, None, 3)
        button_delete_at = Button(DataStructureManager.left_column_x,
                                  start_y + DataStructureManager.control_height * 5 + left_gap * 2,
                                  DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                  'Delete at', BLACK, font25, None, None)
        input_delete_at_index = InputForm(DataStructureManager.left_column_x,
                                          start_y + DataStructureManager.control_height * 6 + left_gap * 2,
                                          DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                          'Enter index', BLACK, font20, None, 3)
        display_delete_returned = TextDisplay(DataStructureManager.left_column_x,
                                              start_y + DataStructureManager.control_height * 7 + left_gap * 2,
                                              DataStructureManager.control_width, DataStructureManager.control_height,
                                              GREY, 'Deleted: ', BLACK, font20, None)

        #  Creating right column of controls
        right_gap = DataStructureManager._calculate_gap(7, 3)
        start_y = DataStructureManager.controls_start_y + right_gap
        button_lin_search = Button(DataStructureManager.right_column_x, start_y, DataStructureManager.control_width,
                                   DataStructureManager.control_height, GREY, 'Linear search', BLACK, font18, None, None)
        input_lin_search_val = InputForm(DataStructureManager.right_column_x,
                                         start_y + DataStructureManager.control_height,
                                         DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                         'Enter value', BLACK, font20, None, 3)
        display_lin_search_returned = TextDisplay(DataStructureManager.right_column_x,
                                                  start_y + DataStructureManager.control_height * 2,
                                                  DataStructureManager.control_width, DataStructureManager.control_height,
                                                  GREY, 'At index: ', BLACK, font20, None)
        button_bin_search = Button(DataStructureManager.right_column_x,
                                   start_y + DataStructureManager.control_height * 3 + right_gap,
                                   DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                   'Binary search', BLACK, font18, None, None)
        input_bin_search_val = InputForm(DataStructureManager.right_column_x,
                                         start_y + DataStructureManager.control_height * 4 + right_gap,
                                         DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                                         'Enter value', BLACK, font20, None, 3)
        display_bin_search_returned = TextDisplay(DataStructureManager.right_column_x,
                                                  start_y + DataStructureManager.control_height * 5 + right_gap,
                                                  DataStructureManager.control_width, DataStructureManager.control_height,
                                                  GREY, 'At index: ', BLACK, font20, None)

        button_sort = Button(DataStructureManager.right_column_x,
                             start_y + DataStructureManager.control_height * 6 + right_gap * 2,
                             DataStructureManager.control_width, DataStructureManager.control_height, GREY,
                             'Sort', BLACK, font20, None, None)
        self._actionable.extend([button_insert, input_insert, button_insert_at, input_insert_at_index,
                                 input_insert_at_value, button_delete_at, input_delete_at_index, button_lin_search,
                                 input_lin_search_val, button_bin_search, input_bin_search_val, button_sort])
        self._text_displays.extend([display_delete_returned, display_lin_search_returned, display_bin_search_returned])