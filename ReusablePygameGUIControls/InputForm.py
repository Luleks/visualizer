from ReusablePygameGUIControls.UIElement import UIElement
from ReusablePygameGUIControls.IActionable import IActionable
import pygame
pygame.font.init()


class InputForm(UIElement, IActionable):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float,
                 color: tuple[int, int, int] | None, text: str, text_color: tuple[int, int, int],
                 font: pygame.sysfont.Font, image_path: str | None, max_len: int):
        super().__init__(x, y, width, height, color, text, text_color, font, image_path)
        self.__default_text = text
        self.__max_len = max_len

    def action(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        super().shift_color(mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.__click(mouse_pos)
        else:
            self.accept_input(event)

    def __click(self, mouse_pos: tuple[int, int]) -> None:
        if super()._is_over(mouse_pos):
            self._active = True
        else:
            self._active = False
        self.__change_text_for_displaying()

    def accept_input(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self._active = False
            elif self._active and event.key == pygame.K_BACKSPACE:
                self._text = self._text[:-1]
            elif self._active and event.key == pygame.K_SPACE:
                self._text += " "
            elif self._active and event.unicode != " " and len(self._text) < self.__max_len:
                self._text += event.unicode

    def __change_text_for_displaying(self) -> None:
        if self._active:
            self._text = ''
        elif not self._active and self._text == '':
            self._text = self.__default_text
