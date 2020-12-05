def threeNumberSum(array, targetSum):
    threeNumberList = list()
    array.sort()
    for i in range(len(array) - 2):
        low = i + 1
        high = len(array) - 1

        while low < high:
            if array[i] + array[low] + array[high] == targetSum:
                threeNumberList.append([array[i], array[low], array[high]])
                low = low + 1
            elif array[i] + array[low] + array[high] < targetSum:
                low = low + 1
            else:
                high = high - 1
    return threeNumberList


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(threeNumberSum(array, targetSum))
