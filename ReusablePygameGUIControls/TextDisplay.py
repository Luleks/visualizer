from ReusablePygameGUIControls.UIElement import UIElement
import pygame
pygame.font.init()


class TextDisplay(UIElement):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float,
                 color: tuple[int, int, int] | None, text: str, text_color: tuple[int, int, int],
                 font: pygame.sysfont.Font, image_path: str | None):
        super().__init__(x, y, width, height, color, text, text_color, font, image_path)
        self.__default_text = text

    def append_text(self, increment: str) -> None:
        """
        Concatenates increment to current displayed text.

        Args:
            increment (str): text to be concatenated.

        Return:
            None
        """
        self._text += increment

    def change_text(self, new_text: str) -> None:
        self._text = new_text

    def reset_text(self) -> None:
        """
        Sets displayed text to it's default value.
        """
        self._text = self.__default_text
