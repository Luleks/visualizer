import pygame.event
from PygameExtensions.CustomEvents import ANIMATION_EVENT
from Managers.DataStructureManager import DataStructureManager
from Windows.DataStructureWindow import DataStructureWindow


class Synchronizer:

    def __init__(self, window: DataStructureWindow, manager: DataStructureManager):
        self._window: DataStructureWindow = window
        self._manager: DataStructureManager = manager
        self._window.accept_rules(self._manager.pack_rules())

    def synchronize(self):
        self._manager.load_rules()
        self._window.accept_rules(self._manager.pack_rules())
        self._manager._method_factory.rules = self._manager._rules

    def animation(self, generator):
        try:
            instruction: dict = next(generator)
            if instruction.get('exception'):
                self._manager.msg_display = instruction.get('exception')
            elif not instruction.get('end'):
                pygame.event.post(pygame.event.Event(ANIMATION_EVENT, generator=generator))
            self._window.accept_rules(self._manager.pack_rules())
            self._window.animation(instruction)
        except Exception as ec:
            self._manager.msg_display = str(ec)
