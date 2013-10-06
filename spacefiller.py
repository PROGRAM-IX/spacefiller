import pygame
from pystroke.game import Game
from sfengines import SFGame, SFMenu

class SpaceFiller (Game):
    def __init__(self, width, height):
        Game.__init__(self, width, height)
        
    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("SpaceFiller")
        self.engines = [SFMenu(self.screen, self.e_e), 
                        SFGame(self.screen, self.e_e)] # add others here
        self.engine = self.engines[0]
        self.run()

def main():
    sf = SpaceFiller(600, 600)
    sf.start()

        
if __name__ == "__main__":
    main()
