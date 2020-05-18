def jumpingOnClouds(c):
    index = 0
    steps = 0
    arraySize = len(c)

    while index < arraySize:
        if (index + 2) < arraySize:
            nextIndex = index + 2
        else:
            nextIndex = index + 1
        
        if nextIndex < arraySize:
            if c[nextIndex] != 1:
                index = index + 2
            else:
                index = index + 1
        else:
            break
        steps = steps + 1
    
    return steps