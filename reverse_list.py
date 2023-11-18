#Two methods to reverse a list.

#1.  Using a stack.
def reverse_list_stack(my_list):

    stack = []
    for el in my_list:
        stack.append(el)
    i = 0
    while len(stack) > 0:
        my_list[i] = stack.pop()
        i += 1

    return my_list
    
#2.  Using two pointers.
def reverse_list_2pointers(my_list):

    i = 0
    j = len(my_list) - 1

    while i <= j:
        temp = my_list[j]
        my_list[j] = my_list[i]
        my_list[i] = temp
        i += 1
        j -= 1

    return my_list

my_list = [1,2,3,4]
#print(reverse_list_stack(my_list))
#print(reverse_list_2pointers(my_list))



















