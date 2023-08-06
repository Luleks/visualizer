from abc import ABC, abstractmethod
from ReusablePygameGUIControls.IActionable import IActionable
from ReusablePygameGUIControls.TextDisplay import TextDisplay
from ReusablePygameGUIControls.IDrawable import IDrawable
import pygame


class UIManager(ABC):

    def __init__(self):
        self._actionable: list[IActionable] = []
        self._text_displays: list[TextDisplay] = []
        self._init_components()

    @abstractmethod
    def _init_components(self):
        pass

    def update_statuses(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        for item in self._actionable:
            item.action(event, mouse_pos)

    @property
    def get_drawable(self) -> list[IDrawable]:
        return self._actionable + self._text_displays
