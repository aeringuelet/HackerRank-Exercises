def countTriplets(arr, r):
    potential2 = {}
    potential3 = {}
    tripletAmount = 0

    for i in arr:
        if i in potential3:
            tripletAmount += potential3.get(i, 0)
        
        if i in potential2:
            potential3[i*r] = potential3.get(i*r, 0) + potential2[i]

        potential2[i*r] = potential2.get(i*r, 0) + 1
    
    return tripletAmount