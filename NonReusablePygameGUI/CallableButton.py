from ReusablePygameGUIControls.Button import Button
from typing import Callable
import pygame
pygame.font.init()


class CallableButton(Button):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float,
                 color: tuple[int, int, int] | None, text: str, text_color: tuple[int, int, int],
                 font: pygame.sysfont.Font, image_path: str | None, function: str):
        super().__init__(x, y, width, height, color, text, text_color, font, image_path)
        self.callable = function

    def action(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        super().shift_color(mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN and super()._is_over(mouse_pos):
            print(self.callable)
