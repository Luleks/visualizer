import pygame
from ReusablePygameGUIControls.Colors.ColorManipulation import ColorManipulation
from ReusablePygameGUIControls.IDrawable import IDrawable
pygame.font.init()


class UIElement(IDrawable):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float,
                 color: tuple[int, int, int] | None, text: str, text_color: tuple[int, int, int],
                 font: pygame.sysfont.Font, image_path: str | None):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._light_color = color
        self._dark_color = ColorManipulation.adjust_color(self._color, 0.9)
        self._text = text
        self._font = font
        self._text_color = text_color
        self._active = False
        if image_path is not None:
            self._image = pygame.transform.scale(pygame.image.load(image_path), (self._width, self._height))
        else:
            self._image = None

    @property
    def text(self):
        return self._text

    def draw(self, win: pygame.Surface) -> None:
        """
        Draws UIElement on pygame surface.

        Args:
            win (pygame.Surface): Surface on which UIElement will be drawn.

        Returns:
            None.
        """

        if self._color is not None and self._active:
            pygame.draw.rect(win, self._dark_color, (self._x, self._y, self._width, self._height))
        elif self._color is not None:
            pygame.draw.rect(win, self._color, (self._x, self._y, self._width, self._height))

        if self._image is not None:
            win.blit(self._image, (self._x, self._y))

        self._blit_text(win)

    def _blit_text(self, win):
        rendered_text = self._font.render(self._text, True, self._text_color)
        text_x = self._x + (self._width - rendered_text.get_width()) // 2
        text_y = self._y + (self._height - rendered_text.get_height()) // 2
        win.blit(rendered_text, (text_x, text_y))

    def _is_over(self, mouse_pos: tuple[int, int]) -> bool:
        return self._x < mouse_pos[0] < self._x + self._width and self._y < mouse_pos[1] < self._y + self._height

    def shift_color(self, mouse_pos: tuple[int, int]) -> None:
        if self._is_over(mouse_pos):
            self._color = self._dark_color
        else:
            self._color = self._light_color

    def invert_state(self) -> None:
        self._active = not self._active
