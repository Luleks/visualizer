import pygame.event

from Commands.Command import Command
from typing import Callable
from ReusablePygameGUIControls.InputForm import InputForm
from PygameExtensions.CustomEvents import ANIMATION_EVENT


class MethodCommand(Command):

    def __init__(self, method: Callable, sources: list[InputForm], data_type):
        self.__method = method
        self.__params = [data_type(source.text) for source in sources]

    def execute(self):
        generator = self.__method(*self.__params)
        animation_event = pygame.event.Event(ANIMATION_EVENT, generator=generator)
        pygame.event.post(animation_event)
