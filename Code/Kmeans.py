def route_np_array(route):
    import numpy as np
    
    #Exclude index 0 - starting point
    route_array = np.array([[loc[0], loc[1]] for loc in route[1:]])
    
    return route_array[:]



def kmean_manhattan(route_array, k, max_steps):
    
    import time
    import numpy as np
    from numpy.random import choice
    import pandas as pd
    from scipy.spatial import distance
    from scipy.spatial.distance import cdist 
    
    #Initial Centers
    samples = choice(len(route_array), size=k, replace=False)
    init_centers = route_array[samples, :]
    centers_new = init_centers

    #print(init_centers)

    #rows x columns
    m,n = route_array.shape

    #Empty Old Center for initial comparison
    centers_old = np.empty((k, n))
    centers_old[:] = np.NaN


    ii = 1  
    while (not np.array_equal(centers_old, centers_new)) and (ii <= max_steps): 

        start_time = time.time()

        centers_old = centers_new

        #Compute Distance
        dist = cdist(route_array, centers_new, metric = 'cityblock')


        #Assign_cluster_labels
        label =  np.argmin(dist, axis=1)


        #Assign new centers, calculate cost
        centers_new = np.empty((k, n))
        centers_new[:] = np.NaN
        cost = 0

        for j in range(k):

            # find index of label
            ind = np.where(label == j)     


            centers_new[j,] = np.median(route_array[ind], axis=0)



        #within-cluster sum-of-squares (WCSS)
        cost = np.sum(np.amin(dist, axis=1))



        end_time = time.time()

        duration = end_time - start_time


        #print("Iteration", ii, "WCSS = ", cost, "Time = ", duration)


        ii += 1


    #print("Stop")
    #print("Iteration", ii, "WCSS = ", cost, "Time = ", duration)
    #print(centers_old)
    #print(centers_new)
    
    return route_array, k, m, label, centers_new





def route_output(route, label, k):
    
    final_route = [[(33.9697702, -83.96162849999999), ] for _ in range(1, k+1)]

    for i,j in zip(label, route[1:]):
        final_route[i].append(j)

    return final_route[:]