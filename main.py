from Main.Module import Module
from Main.ConcreteFactory import ConcreteFactory
import pygame


if __name__ == '__main__':
    manager_factory: ConcreteFactory = ConcreteFactory()
    module: Module = Module(manager_factory)
    module.run()
    pygame.quit()
