from pystroke.game_engine import GameEngine
from pystroke.event_engine import EventEngine
from pystroke.input_engine import InputEngine
from pystroke.hud import HUDText
from pystroke.vector2 import Vector2
from pystroke.vex import Vex
import pygame
from pygame.locals import *

class SFGame(GameEngine):
    def __init__(self, screen, event_e=EventEngine(InputEngine()), fps=60):
        GameEngine.__init__(self, screen, event_e, fps)
        self.cursor = Vex(300, 300, pygame.Color(255, 255, 255), 
                        (Vector2(0, -10), Vector2(0, 10), Vector2(0, 0),
                        Vector2(-10, 0), Vector2(10, 0), 
                        Vector2(0, 0)), 2)
        self.outer_frame = Vex(300, 300, pygame.Color(255, 255, 255),
                        (Vector2(-300, -300), Vector2(300, -300),
                        Vector2(300, 300), Vector2(-300, 300)), 2)
        self.fillers = []
        self.justcreated = True
        #self.test = Vex(400, 400, pygame.Color(255, 0, 0),
         #               (Vector2(-10, -10), Vector2(10, -10),
          #              Vector2(10, 10), Vector2(-10, 10)), 0)
        
    def update(self):
        self.event_e.update()
        self.clock.tick(self.FPS)
        
        self.cursor.x, self.cursor.y = self.event_e.input.mouse_pos
        print self.cursor.x, self.cursor.y
        if self.cursor.x == 1 and self.cursor.y == 1:
            self.cursor.x, self.cursor.y = 300, 300
        
        if self.event_e.input.mouse_buttons[1]:
            if not self.justcreated:
                self.fillers.append(Vex(self.cursor.x, self.cursor.y, pygame.Color(255, 0, 0), 
                                    (Vector2(-10, -10), Vector2(10, -10),
                                    Vector2(10, 10), Vector2(-10, 10)), 0))
                self.justcreated = True
            else:
                f = self.fillers[-1]
                for pt in f.get_absolute_points_vector2():
                    if not self.outer_frame.point_inside(pt):
                        return 0
                    for other in self.fillers[:-1]:
                        if other.point_inside(pt):
                            return 0
                f.scale_x = f.scale_x + 0.5
                f.scale_y = f.scale_y + 0.5
        
        else:
            self.justcreated = False
            if len(self.fillers) >= 1:
                f = self.fillers[-1]
                f.colour = pygame.Color(0, 255, 0)
        
        if self.get_key(K_SPACE):
            del self.fillers
            self.fillers = []
        
        
        # To switch state
        if self.get_key(K_ESCAPE):
            print "Quitting game"
            return 0

        # To quit 
        #elif quit_condition:
        #    return 1

        # To maintain consistency
        #else:
        #    return 2

        return 2

    def draw(self):
        self.draw_e.begin_draw(pygame.Color(0, 0, 0))
        # Draw your drawables here
        # They must be passed in as lists
        # self.draw_e.draw([some_drawable, some_other_drawable])
        # self.draw_e.draw([another_drawable])
        self.draw_e.draw(self.fillers)
        self.draw_e.draw([self.outer_frame])
        self.draw_e.draw([self.cursor])
        self.draw_e.draw([self._hud])
        self.draw_e.end_draw()
        
        
class SFMenu(GameEngine):
    def __init__(self, screen, event_e=EventEngine(InputEngine()), fps=60):
        GameEngine.__init__(self, screen, event_e, fps)
        self._hud.add(HUDText("title", pygame.Color(50, 50, 50),
                                "space filler", (50, 300), 3, 2, True))
        self.blah = [HUDText("blah1", pygame.Color(255, 255, 255),
                            "BLAH", (0,0), 3, 3, True)]
        
    def update(self):
        self.event_e.update()
        self.clock.tick(self.FPS)
        # To switch state
        if self.get_key(K_RETURN):
            print "Entering game from menu"
            return 0
        
        # To quit 
        elif self.get_key(K_q):
            print "Quitting from menu"
            return 1
        
        # To maintain consistency
        #else:
        #    return 2
        
        return 2

    def draw(self):
        self.draw_e.begin_draw(pygame.Color(255, 255, 0))
        # Draw your drawables here
        # They must be passed in as lists
        # self.draw_e.draw([some_drawable, some_other_drawable])
        # self.draw_e.draw([another_drawable])
        self.draw_e.draw([self._hud])
        self.draw_e.end_draw()
