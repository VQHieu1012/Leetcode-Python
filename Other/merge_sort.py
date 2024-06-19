def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    leftSorted = mergeSort(leftArr)
    rightSorted = mergeSort(rightArr)
    print("left sorted: ", leftSorted)
    print("right sorted: ", rightSorted)

    return merge(leftSorted, rightSorted)

def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

