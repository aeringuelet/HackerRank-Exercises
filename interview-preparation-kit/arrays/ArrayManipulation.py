def arrayManipulation(n, queries):
    resultArray = [0] * n

    for [a, b, k] in queries:
        resultArray[a - 1] += k
        if b < n: resultArray[b] -= k 

    maxValue = tempRes = 0
    for i in resultArray:
        tempRes += i
        if tempRes > maxValue:
            maxValue = tempRes

    return maxValue