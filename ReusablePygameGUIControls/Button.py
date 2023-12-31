from ReusablePygameGUIControls.UIElement import UIElement
from ReusablePygameGUIControls.IActionable import IActionable
from abc import abstractmethod
import pygame
pygame.font.init()


class Button(UIElement, IActionable):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float,
                 color: tuple[int, int, int] | None, text: str, text_color: tuple[int, int, int],
                 font: pygame.sysfont.Font, image_path: str | None):
        super().__init__(x, y, width, height, color, text, text_color, font, image_path)

    @abstractmethod
    def action(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        pass
