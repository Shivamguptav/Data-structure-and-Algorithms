def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def qs(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        qs(arr, low, pIndex - 1)
        qs(arr, pIndex + 1, high)

def quickSort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr

