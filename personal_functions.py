
def binary_search(arr, el):
    L=0
    R=len(arr)-1
    while(L<=R):
        mid = L + (R - L) // 2
        if(arr[mid]==el):
            return mid
        elif(arr[mid]<el):
            L=mid+1
        else:
            R=mid-1
    return -1


