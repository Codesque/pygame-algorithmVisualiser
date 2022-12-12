import pygame 
from settings import * 
from warshall import *
from sprites import BoundingBox
import time 
pygame.init() 
pygame.font.init()




class Visualization: 

    def __init__(self , state : bool  , screen : pygame.Surface , set_d_T) -> None:
        self.state = state  
        self.set_d_T = set_d_T # method
        self.d_T = 0.1
        self.screen = screen 
        self.createBbox = True 
        self.initialise_warshall() 
        self.initialiseGraph() 
        self.initialise_matrixRects()
        self.bboxGroup = pygame.sprite.Group() 
        self.initialise_bbox()
        



        
        
    def initialise_warshall(self): 
        warshLog = [] 
        self.adjacencyMatrix = createAdjacencyMatrix() 
        print(self.adjacencyMatrix)
        self.warshall_log = warshall(self.adjacencyMatrix  , warshLog)
        self.matrixRects = []  


    def quit(self): 
        self.state = False 

    def controlls(self): 
        
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN: 
                if event.key == LEVEL_EXIT :
                    self.quit() 

    def renderText(self , rect : pygame.Rect ,txt = "None"): 
        myFont = pygame.font.SysFont(FONT_TYPE , FONT_W , FONT_H) 
        text = myFont.render(txt ,False , MATRIX_FONT_COLOR) 
        w , h = text.get_width() , text.get_height() 
        self.screen.blit(text , (rect.centerx - w//2 , rect.centery - h//2 , rect.w , rect.h))  

    def initialise_bbox(self): 

            first_pos = pygame.math.Vector2(self.matrixRects[0].topleft)
            bbox = BoundingBox('ij', first_pos , self.warshall_log ,self.matrixRects, len(self.adjacencyMatrix[0][:]) ,self.d_T , self.renderNodeText) 
            self.bboxGroup.add(bbox) 
            
            
    def initialise_matrixRects(self):
        n = len(self.adjacencyMatrix[0][:])
        for i in range(n): 
            for j in range(n): 
                x = SYSTEM_BLANK + j * SQUARE_WIDTH 
                y = BLANK_Y + SYSTEM_BLANK + i * SQUARE_HEIGHT 
                rect = pygame.draw.rect(self.screen ,SYSTEM_BG_COLOR , pygame.Rect(x , y , SQUARE_WIDTH , SQUARE_HEIGHT) , SQUARE_BORDER  ) 
                self.matrixRects.append(rect)  


    def displayMatrix(self): 
        n = len(self.adjacencyMatrix[0][:])   
        for i in range(n): 
            for j in range(n): 
                print(len(self.matrixRects))
                rect = self.matrixRects[(i) * n + j] 
                self.renderText(rect , str(self.adjacencyMatrix[i][j]))  
                

        



    def initialiseGraph(self): 
        graphDict = {}
        n = len(self.adjacencyMatrix[0][:]) 
        for i in range(n): 
            graphDict[i] = [] 

        for i in range(n): 
            for j in range(n): 
                if (self.adjacencyMatrix[i][j] == 1) and (i != j) : 
                    (graphDict[i]).append(j)

        print(graphDict)
        self.graphDict = graphDict 
        self.graphRects = []
        self.randomLinkageColors = []


    def displayAsGraph(self):
        n = len(self.adjacencyMatrix[0][:])   

        GRAPH_X , GRAPH_Y = SYSTEM_BLANK + (WIDTH//3) , SYSTEM_BLANK
        GRAPH_SQUARE_WIDTH , GRAPH_SQUARE_HEIGHT = ((WIDTH//2) / n ) , ((HEIGHT//2) / n )
        i  = 0 
        while (i <  n): 

            x = GRAPH_X + i * GRAPH_SQUARE_WIDTH

            rect1 = pygame.draw.rect(self.screen , 
            SYSTEM_BG_COLOR , pygame.Rect(x , GRAPH_Y , GRAPH_SQUARE_WIDTH , GRAPH_SQUARE_HEIGHT) , SQUARE_BORDER )

            rect2 = pygame.draw.rect(self.screen , 
            SYSTEM_BG_COLOR , pygame.Rect(x , GRAPH_Y + GRAPH_SQUARE_HEIGHT , GRAPH_SQUARE_WIDTH , GRAPH_SQUARE_HEIGHT) , SQUARE_BORDER )

            if i % 2 == 0 : 
                self.graphRects.append(rect1) 
                self.graphRects.append(rect2) 
            else : 
                self.graphRects.append(rect2) 
                self.graphRects.append(rect1) 

            i += 1

        j = 0
        while ( j < n): 
            center = self.graphRects[2*j].center 
            radius = (GRAPH_SQUARE_WIDTH//2) - 4
            pygame.draw.circle(self.screen , CIRCLE_COLOR , center , radius , SQUARE_BORDER  )
            self.renderText(self.graphRects[2*j] , str(j)) 

            j += 1

    def renderNodeText(self): 
        j = 0 
        n = len(self.adjacencyMatrix[0][:]) 

        while (j < n):
            self.renderText(self.graphRects[2*j] , str(j)) 
            j += 1 

        

    def displayGraphLinks(self): 
        

        

            
        
        for key in self.graphDict : 

            if self.randomLinkageColors == [] : 
                for key in self.graphDict : 
                    for link in self.graphDict[key]: 
                        r = random.randint(0,255) 
                        g = random.randint(0,255)
                        b = random.randint(0,255)
                        self.randomLinkageColors.append((r ,g , b))
            
            if self.graphDict[key] == [] : 
                continue 
            else : 
                k = 0 
                for nodeKey in self.graphDict[key] : 
                    
                    
                    cond1 = (key %2 == 0) 
                    cond2 = (nodeKey % 2 == 0) 

                    if cond1 and cond2 : 
                        middle_x = ( self.graphRects[ 2 *key].centerx  + self.graphRects[2 * nodeKey].centerx) // 2   
                        middle_y = self.graphRects[2 *key].centery  
                        corner_y = middle_y - CORNER_BLANK
                        pygame.draw.line(self.screen , self.randomLinkageColors[k] , self.graphRects[2*key].center , (middle_x , corner_y) ,LINKAGE_BORDER )  
                        pygame.draw.line(self.screen , self.randomLinkageColors[k] , (middle_x , corner_y) , self.graphRects[2*nodeKey].center , LINKAGE_BORDER) 


                    elif cond1 != cond2 :  
                        pygame.draw.line(self.screen , self.randomLinkageColors[k] , self.graphRects[2*key].center , self.graphRects[2*nodeKey].center , LINKAGE_BORDER) 

                    else : 
                        middle_x = ( self.graphRects[ 2 *key].centerx  + self.graphRects[2 * nodeKey].centerx) // 2   
                        middle_y = self.graphRects[2 *key].centery  
                        corner_y = middle_y + CORNER_BLANK
                        pygame.draw.line(self.screen , self.randomLinkageColors[k] , self.graphRects[2*key].center , (middle_x , corner_y) ,LINKAGE_BORDER  )  
                        pygame.draw.line(self.screen , self.randomLinkageColors[k] , (middle_x , corner_y) , self.graphRects[2*nodeKey].center , LINKAGE_BORDER)


                    k += 1



    def display(self): 
        

        self.d_T =  time.time()
        while self.state : 

            self.controlls()
            self.screen.fill(SYSTEM_BG_COLOR) 
            
            self.displayAsGraph() 
            self.displayGraphLinks()
            self.renderNodeText()
            self.displayMatrix()  
            self.bboxGroup.draw(self.screen) 

            
            self.bboxGroup.update()
            self.d_T = time.time() - self.d_T
            self.set_d_T(self.d_T)
            pygame.display.update()  

            



