from ReusablePygameGUIControls.Button import Button
from Commands.Command import Command
import pygame
pygame.font.init()


class CommandButton(Button):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float,
                 color: tuple[int, int, int] | None, text: str, text_color: tuple[int, int, int],
                 font: pygame.sysfont.Font, image_path: str | None, command: Command | None):
        super().__init__(x, y, width, height, color, text, text_color, font, image_path)
        self._command = command

    def action(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        super().shift_color(mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN and super()._is_over(mouse_pos) and self._command is not None:
            self._command.execute()
