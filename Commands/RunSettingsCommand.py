import pygame.event
from Commands.Command import Command
from PygameExtensions.CustomEvents import SETTINGS_CHANGED_EVENT
import subprocess
import os


class RunSettingsCommand(Command):

    def __init__(self, exe_file_name: str):
        self._exe_name = exe_file_name

    def execute(self):
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        settings_dir = os.path.join(script_dir, 'Settings', self._exe_name, 'bin', 'Debug')
        os.chdir(settings_dir)
        executable_relative = os.path.join(f'{self._exe_name}.exe')
        executable = os.path.join(settings_dir, executable_relative)

        _ = subprocess.run(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        settings_changed = pygame.event.Event(SETTINGS_CHANGED_EVENT, custom_attribute=settings_dir +
                                                                                       f'{self._exe_name}.xml')
        pygame.event.post(settings_changed)
        os.chdir(script_dir)
