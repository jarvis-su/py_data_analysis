
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # print(len(arr)/2)
    # print(type(int(len(arr)/2)))
    index = int(len(arr)/2)
    pivot = arr[index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    array = [3,5,6,7,8,9,1,7]
    l = quicksort(array)
    print(l)