def mergeSort(arr, n):
    # Write your code here.
    if n <= 1:
        return arr

    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left, len(left))
    mergeSort(right, len(right))

    i = j = k = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j+=1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr
