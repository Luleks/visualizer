import pygame
from NonReusablePygameGUI.DataStructureBlock import DataStructureBlock
from ReusablePygameGUIControls.Colors.ColorConstants import *
pygame.font.init()


class ArrayBlock(DataStructureBlock):
    font = None

    def __init__(self, x: int, y: int, width: int, height: int, value: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        ArrayBlock.font = pygame.font.SysFont('comicsans', int(self.height * 0.6))
        self.rendered_text = ArrayBlock.font.render(str(value), True, WHITE)
        self.red = False

    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, GREY, (self.x, self.y, self.width, self.height))
        if self.red:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height), 3)
        else:
            pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 3)
        win.blit(self.rendered_text, (self.x + (self.width - self.rendered_text.get_width()) // 2,
                                      self.y + (self.height - self.rendered_text.get_height()) // 2))
