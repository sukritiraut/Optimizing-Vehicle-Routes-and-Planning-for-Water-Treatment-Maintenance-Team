# Version 2, solve memory issue. Only keep the best route by comparing previous and current to get minimum

#####################################################################################
## Note: There could be more than 1 optimal route, the alog only pull the last one ##
#####################################################################################


def brute_force(dist_matrix, dura_matrix):
    
    
    import pandas as pd
    import numpy as np
    from itertools import combinations, permutations
    import time
    from datetime import datetime
    from math import factorial

    # from utils2 import get_matrix_from_api
    
    
    route = dist_matrix[0, :]
    
    # Get all the comb as generator intead of list
     
    # l = [i for i in range(0, len(route))]
    # all_routes = (i + (0,) for i in permutations(l) if i[0] == 0) # this will generate all combinations
   
   
    # Only need one start with 0, factorial(len)/len
    l = [i for i in range(1, len(route))]
    all_routes = ((0,) + i + (0,) for i in permutations(l))
    
    
    # Calculate total distance per route
    route = []
    distance = []
    previous = 0
    current = 0
    
    for index, r in enumerate(all_routes):

        #print(index, r)

        end = len(r)


        # Calcualte total distance for a route
        total = 0
        for i, j in zip(r[0:end-1], r[1:end]):

            total += dist_matrix[i][j]


        current = total


        # Initial route 
        if previous == 0:

            route.append(r)
            distance.append(total)
            previous = current
        
        # Rest
        elif current < previous: 

            route[0] = r
            distance[0] = total
            previous = current
            
        
    # Calculate duration
    dura = 0
    r = route[0]
    end = len(route[0])
    for i, j in zip(r[0:end-1], r[1:end]):
        
        dura += dura_matrix[i][j]
        
    
    route = list(route[0])
    distance = round(distance[0] / 1609)
    duration = round(dura / 60)
        
    
    
    return route, distance, duration

