import random
def createAdjacencyMatrix(adjacencyMatrix = None ):  

    def getRandom(): 
        return random.choice([1,1,1,0,0,0,0,0,0,0]) 

    length = random.randint(3 , 8)  
    adjacencyMatrix = [[getRandom() for j in range(length)] for i in range(length)]
    return adjacencyMatrix


    



def warshall( adjacencyMatrix , warshall_log : list ): 

    length = len(adjacencyMatrix[0][:]) 

    copy_adj = [[ adjacencyMatrix[i][j] for j in range(length)] for i in range(length)]

    for k in range(length): 
        for i in range(length): 
            for j in range(length): 

                if copy_adj[i][j] == 0: 

                    if ( copy_adj[i][k] and copy_adj[k][j] ) : 
                        copy_adj[i][j] = 1 
                        warshall_log.append(["CHANGE_SUCCESSFULL" , i , j , k]) 

                    else : 
                        warshall_log.append(["CHANGE_UNSUCCESSFULL" , i , j , k])  

                else : 
                    warshall_log.append(["IGNORED" , i , j , k])  

    return warshall_log 


                



