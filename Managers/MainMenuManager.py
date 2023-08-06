from Managers.UIManager import UIManager
from ReusablePygameGUIControls.TextDisplay import TextDisplay
from ReusablePygameGUIControls.Button import Button
from ReusablePygameGUIControls.Colors.ColorConstants import *
from PygameExtensions.Fonts import *
from Constants.ScreenConstants import *
from Commands.RedirectCommand import RedirectCommand


class MainMenuManager(UIManager):

    def __init__(self):
        super().__init__()

    def _init_components(self):
        title = TextDisplay(0, 0, 1200, 100, None, 'DATA STRUCTURES VISUALISER VER 1.2', WHITE, font50, None)
        self._text_displays.append(title)

        buttons_text = ['array', 'string', 'linked list', 'stack', 'queue', 'hash table', 'tree', 'graph']

        allocated_y = 100  # Title text display
        button_width = 150
        button_height = 150
        buttons_in_row = 4
        buttons_in_column = 2
        gap_x = button_width // 3
        gap_y = button_height // 2

        start_gap_x = (SCREEN_WIDTH - buttons_in_row * button_width - (buttons_in_row - 1) * gap_x) // 2
        start_gap_y = (SCREEN_HEIGHT - allocated_y - buttons_in_column * button_height -
                       (buttons_in_column - 1) * gap_y) // 2

        for i in range(len(buttons_text)):
            button_x = start_gap_x + (gap_x + button_width) * (i % 4)
            button_y = start_gap_y + (gap_y + button_height) * (i // 4)
            b = Button(button_x, button_y + 100, button_width, button_height, GREY, buttons_text[i],
                       BLACK, font25, None, RedirectCommand(buttons_text[i].replace(' ', '_')))
            self._actionable.append(b)
