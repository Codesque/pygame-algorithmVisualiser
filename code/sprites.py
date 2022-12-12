import pygame 
from settings import *
pygame.init() 


class BoundingBox(pygame.sprite.Sprite): 
    def __init__(self , bbtype : str ,first_pos : pygame.Vector2 , instructions : list , matrixRects : list  , length , delta_time , blit_nodeText : object) -> None:
        super().__init__() 
        self.len = length
        self.bbType = bbtype # could be 'ij' or 'k'
        self.matrixRects = matrixRects
        self.rect = pygame.Rect(first_pos.x , first_pos.y , SQUARE_WIDTH , SQUARE_HEIGHT ) 
        self.pos = pygame.math.Vector2(self.rect.center) 
        self.image =  pygame.image.load("assets\duckShooting\PNG\HUD\crosshair_red_large.png") 
        self.direction = pygame.math.Vector2(0,0) 
        self.vx , self.vy = 10000 , 10000 
        self.d_T = delta_time

        cW , cH = 10 , 10 
        self.collusionRect = pygame.rect.Rect(self.rect.centerx , self.rect.centery , cW , cH) 

        self.instructions = instructions
        self.orderNumber = 0
        self.preI , self.preJ = -1 , -1 

        self.renderTxt = blit_nodeText 
        self.screen = pygame.display.get_surface()
        

    def go(self , x = 0.0 , y = 0.0): 
        
        rx = self.vx * self.d_T * x 
        ry = self.vy * self.d_T * y
        self.pos += pygame.math.Vector2(rx , ry) 
        self.rect.center = self.pos
        self.collusionRect.center = self.rect.center


    def go_forward(self , destRect : pygame.rect.Rect): 

        try:
            if self.collusionRect.collidepoint(destRect.center): 
                x = (destRect.centerx - self.collusionRect.centerx)
                y = (destRect.centery - self.collusionRect.centery)

                self.go(x , y) 
        except: 
            pass 


        

    def go_reset(self , i , j , k): 
        
        
        self.go_forward(self.matrixRects[int(i+1)* self.len - 1]) 
        self.go_forward(self.matrixRects[int(i) * self.len + int(j)])  





    def instr_IGNORED(): 
        pass 


    def instr_CHANGE_UNSUCCESS():
        pass 


    def instr_CHANGE_SUCCESS(): 
        pass 
        
    def increase_orderNumber(self): 
        if self.orderNumber < len(self.instructions): 
            self.orderNumber += 1 

    def applyInstructions(self): 
        
           
        inst_data  = self.instructions[self.orderNumber] 
        if isinstance(inst_data , list) : 
            status = inst_data[0] 
            i = inst_data[1] 
            j = inst_data[2] 
            k = inst_data[3] 

        if self.preJ > j : # column up  
            if self.preI > i : 
                pygame.quit() 
            else : 
                self.go_reset(i , j , k) 

        if status == "CHANGED_SUCCESSFULL": 
            self.go_forward(self.matrixRects[(int(i) )* self.len + int(j) + 1 ]) 
        elif status == "CHANGED_UNSUCCESSFULL": 
            self.go_forward(self.matrixRects[(int(i) )* self.len + int(j) + 1 ]) 
        elif status == "IGNORED": 
            self.go_forward(self.matrixRects[(int(i) )* self.len + int(j) + 1 ]) 

        self.preI , self.preJ = i , j 
        return self.increase_orderNumber()


                

    def update(self) -> None: 
        self.applyInstructions()



        