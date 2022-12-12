
import pygame 
pygame.init() 

from level import Visualization 



class ProgramManager: 

    def __init__(self , screen : pygame.Surface ,set_d_T) -> None:

        self.set_d_T = set_d_T 
        self.screen = screen 
        self.status = "WARSHALL" 
        self.level_WARSHALL = Visualization(True ,self.screen, self.set_d_T) 


    def run(self): 
        if self.status == "WARSHALL": 
            self.level_WARSHALL.display() 



