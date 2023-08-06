from abc import ABC, abstractmethod
import pygame


class IActionable(ABC):

    @abstractmethod
    def action(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        pass
