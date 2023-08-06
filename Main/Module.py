import pygame.event
from Main.AbstractFactory import AbstractFactory
from PygameExtensions.CustomEvents import *


class Module:

    def __init__(self, factory: AbstractFactory):
        self.__factory: AbstractFactory = factory
        self.__manager, self.__window = self.__factory.produce()

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == DATASTRUCT_CHANGE_EVENT:
                    self.__manager, self.__window = self.__factory.produce(event.custom_attribute)

                self.__manager.update_statuses(event, pygame.mouse.get_pos())

            self.__window.draw(self.__manager.get_drawable)
