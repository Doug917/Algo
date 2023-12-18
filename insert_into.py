# Insert element at position i<=len(arr) of array arr.
# Mimics the built-in python method List.insert.
arr = [1,3,7,9,1]
i = 3
el = 0
def insert_arr(arr, i, element):
    
    j = 0
    while j < i:
        j += 1
        
    arr.append(0)
    last = len(arr) - 1
    while last > j:
        arr[last] = arr[last-1]
        last -= 1
        
    arr[j] = element
    print(arr)

#test
insert_arr(arr, i, el)
