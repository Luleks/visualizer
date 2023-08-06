import pygame.event
from Commands.Command import Command
from PygameExtensions.CustomEvents import *


class RedirectCommand(Command):

    def __init__(self, new_module_name: str):
        self.new_module = new_module_name

    def execute(self):
        module_change_event = pygame.event.Event(MANAGER_CHANGE_EVENT, custom_attribute=self.new_module)
        pygame.event.post(module_change_event)
