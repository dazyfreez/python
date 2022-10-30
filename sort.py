
def sort():
    # this will sort the list
    # and return the sorted list
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("unsorted list: " + str(list))
    list.sort() # this will sort the list

def sort_list_by_yourself():
    # now we will write a sorting algorithm
    # by ourself
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("unsorted list: " + str(list))
    # now we will sort the list
    # we will use the bubble sort algorithm
    # we will use a while loop
    while True:
        # we will use a for loop
        for i in range(len(list) - 1):
            # now we will compare the numbers
            if list[i] > list[i + 1]:
                # now we will swap the numbers
                list[i], list[i + 1] = list[i + 1], list[i]
                break
        else:
            # now we will print the sorted list
            print("sorted list: " + str(list))
            break

def sort_list_by_length():
    # now we will sort a list by the length of the strings
    # we will use the sorted function
    list = ["hello", "world", "this", "is", "a", "list", "of", "strings"]
    print("unsorted list: " + str(list))
    # now we will sort the list
    list = sorted(list, key=len)
    # now we will print the sorted list
    print("sorted list: " + str(list))