def nearest_neighbor(dist_matrix, dura_matrix):

    import pandas as pd
    import numpy as np
    from itertools import combinations, permutations
    import time
    from datetime import datetime
    from math import factorial
    import math

    trips = len(dist_matrix)


    # replace 0 with 999, so it won't look at it own location
    dist_matrix = np.divide(dist_matrix, 1609) # convert to miles
    dist_matrix2 = dist_matrix.copy()
    #dist_matrix2[dist_matrix2 == 0] = 999
    np.fill_diagonal(dist_matrix2, 999)     # may go back to same place 

    #print(dist_matrix2)

    #print(dist_matrix[1,[1,2]]) # 1,1  1,2 
    #print(dist_matrix[0,[1,2]]) # 0,1 0,

    loc = [i for i in range(len(dist_matrix[0,:]))]

    i = 1
    current = 0
    distance = 0
    route = []
    route.append(current)

    # Getting the minimum distance from current -> next
    while i < trips:


        # Initial 
        if i == 1:

            next_shortest = np.argmin(dist_matrix2[current, :])

            route.append(next_shortest)
            distance += dist_matrix2[current,next_shortest]
            current = next_shortest

        #Rest    
        else:
            dist_matrix_next = dist_matrix2[current,:]
            visited = np.isin(loc, route)
            dist_matrix_next[visited] = 999

            #print(dist_matrix_next)

            next_shortest = np.argmin(dist_matrix_next)
            route.append(next_shortest)
            distance += dist_matrix_next[next_shortest]
            current = next_shortest


        i+=1
        #print(current)
        #print(route)


    # Adding first loc to the end  
    route.append(0)
    distance += dist_matrix2[current, 0]
    #print(dist_matrix2[current, 0])
    
    
    # Calculate duration
    dura = 0
    r = route
    end = len(route)
    for i, j in zip(r[0:end-1], r[1:end]):
        
        dura += dura_matrix[i][j]
        
    
    route = list(route)
    distance = round(distance)
    duration = round(dura / 60)
    
    
    
    
    return route, distance, duration




# https://blog.devgenius.io/traveling-salesman-problem-nearest-neighbor-algorithm-solution-e78399d0ab0c

def solve_tsp_nearest(distances):


    import pandas as pd
    import numpy as np
    from itertools import combinations, permutations
    import time
    from datetime import datetime
    from math import factorial
    import math

    
    start_time = time.time()
    
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0
    
    # Start at the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    
    # Repeat until all cities have been visited
    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        # Move to the nearest city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += distances[current_city][0]
    
    total_distance = round(total_distance / 1609)

    return tour, total_distance