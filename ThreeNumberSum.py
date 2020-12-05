def threeNumberSum(array, targetSum):
    array.sort()
    threeSumList = list()
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            x = targetSum - (array[i] + array[j])

            temp_array = list(array)
            temp_array.remove(array[i])
            temp_array.remove(array[j])

            index_x = binarysearch(temp_array, 0, len(temp_array)-1, x)
            if index_x != -1:
                temp_list = [array[i], array[j], temp_array[index_x]]
                temp_list.sort()

                if temp_list not in threeSumList:
                    threeSumList.append(temp_list)

    return threeSumList


def binarysearch(array, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if x == array[mid]:
            return mid

        elif x < array[mid]:
            return binarysearch(array, low, mid - 1, x)

        else:
            return binarysearch(array, mid + 1, high, x)
    else:
        return -1
