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
