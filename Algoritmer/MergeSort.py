def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    # Skapa sub-listor (skapar nya objekt i minnet, precis som Java ArrayList)
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result