import pygame
from ReusablePygameGUIControls.UIElement import IDrawable
from abc import ABC
from Constants.ScreenConstants import *


class Window(ABC):
    workspace_x = 140
    workspace_y = 200
    workspace_width = 920
    workspace_height = 490

    def __init__(self, background_color: tuple[int, int, int] | None, background_image_path: str | None):
        self._background_color = background_color
        self._background_image = pygame.image.load(background_image_path) if background_image_path is not None else None
        self._win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('DataStructuresVisualizer')

    def __draw_background(self) -> None:
        if self._background_color is None:
            self._win.blit(self._background_image, (0, 0))
        else:
            self._win.fill(self._background_color)

    def draw(self, ui_elements: list[IDrawable]) -> None:
        self.__draw_background()

        for ui_element in ui_elements:
            ui_element.draw(self._win)

        pygame.display.update()
