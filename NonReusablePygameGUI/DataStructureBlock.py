from abc import abstractmethod
from ReusablePygameGUIControls.IDrawable import IDrawable
from pygame import Surface


class DataStructureBlock(IDrawable):

    @abstractmethod
    def draw(self, win: Surface) -> None:
        pass
