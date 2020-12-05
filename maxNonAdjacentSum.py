def maxSubsetSumNoAdjacent(array):

    if len(array) == 0:
        return 0
    elif len(array) <= 2:
        return max(array)

    sumarray = []
    for i in range(len(array)):
        sumarray.append(0)
    sumarray[0] = array[0]
    sumarray[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        sumarray[i] = max(sumarray[i-1], sumarray[i-2] + array[i])
        print(sumarray)
    return sumarray[-1]

array = [4, 3, 5, 200, 5, 3]
maxSubsetSumNoAdjacent(array)
