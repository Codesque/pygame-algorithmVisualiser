import pygame 
from settings import * 
from manager import ProgramManager


class Program : 

    def __init__(self) -> None:
        
        pygame.init() 
        pygame.display.set_caption("Visualization of Warshall Algorithm")
        self.screen = pygame.display.set_mode( (WIDTH , HEIGHT) ) 
        self.running = True 
        self.zoomScale = 1 
        self.d_T = 1

    def set_d_T(self , value): 
        self.d_T = value 



    def execute(self):  
        manager = ProgramManager(self.screen,self.set_d_T) 
        manager.run() 
        



if __name__ == "__main__": 
    program = Program() 
    program.execute() 





