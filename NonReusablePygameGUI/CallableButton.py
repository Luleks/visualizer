from ReusablePygameGUIControls.Button import Button
from ReusablePygameGUIControls.InputForm import InputForm
import pygame
from DataStructures.MethodFactory import MethodFactory
from Commands.MethodCommand import MethodCommand
pygame.font.init()


class CallableButton(Button):

    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float,
                 color: tuple[int, int, int] | None, text: str, text_color: tuple[int, int, int],
                 font: pygame.sysfont.Font, image_path: str | None, function: str, method_factory: MethodFactory,
                 sources: list[InputForm], data_type: type | None):
        super().__init__(x, y, width, height, color, text, text_color, font, image_path)
        self.callable = function
        self.method_factory = method_factory
        self.sources = sources
        self.data_type = data_type

    def action(self, event: pygame.event.Event, mouse_pos: tuple[int, int]) -> None:
        super().shift_color(mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN and super()._is_over(mouse_pos):
            method = self.method_factory.produce(self.callable)
            command = MethodCommand(method, self.sources, self.data_type)
            command.execute()
