def find_smallest_number(list1):
    smallest = list1[0] 
    for i in range(1, len(list1)):
        if list1[i] < smallest:
            smallest = list1[i] 
    return smallest
list1 = [5, 7, 9, 14, 10, 20, 4]
print("The smallest number in the list is:", find_smallest_number(list1))
