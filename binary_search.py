#binary serach function that works with duplicates.
def binary_search(keys, query):

    
    if keys[0] == query:
        return 0
    low, high = 0, num_keys - 1
    mid = (low+high)//2
    stored_val = num_keys
    while low<=high:
        if keys[mid] < query:   
            low = mid+1
            mid = (low+high)//2
        else:
            high = mid
            mid = (low+high)//2
            if keys[mid]==query:
                stored_val = min(stored_val,mid)
            if low==high:
                break
            
    if stored_val==num_keys:
        return -1
    else:
        return stored_val


