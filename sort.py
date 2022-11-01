
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

def sort_list_by_length_and_alphabetically():
    # now we will sort a list by the length of the strings
    # and alphabetically
    # we will use the sorted function
    list = ["hello", "world", "this", "is", "a", "list", "of", "strings"]
    print("unsorted list: " + str(list))
    # now we will sort the list
    list = sorted(list, key=len)
    # now we will sort the list alphabetically
    list = sorted(list)
    # now we will print the sorted list
    print("sorted list: " + str(list))

def sort_list_by_length_and_alphabetically_and_reverse():
    # now we will sort a list by the length of the strings
    # and alphabetically
    # we will use the sorted function
    list = ["hello", "world", "this", "is", "a", "list", "of", "strings"]
    print("unsorted list: " + str(list))
    # now we will sort the list
    list = sorted(list, key=len)
    # now we will sort the list alphabetically
    list = sorted(list)
    # now we will reverse the list
    list.reverse()
    # now we will print the sorted list
    print("sorted list: " + str(list))

def sort_list_by_length_and_alphabetically_and_reverse_and_print():
    # now we will sort a list by the length of the strings
    # and alphabetically
    # we will use the sorted function
    list = ["hello", "world", "this", "is", "a", "list", "of", "strings"]
    print("unsorted list: " + str(list))
    # now we will sort the list
    list = sorted(list, key=len)
    # now we will sort the list alphabetically
    list = sorted(list)
    # now we will reverse the list
    list.reverse()
    # now we will print the sorted list
    print("sorted list: " + str(list))
    # now we will print the list
    for i in list:
        print(i)

print("welcome to the sorting algorithmus")
print("please choose an option")
print("1. sort a list")
print("2. sort a list by yourself")
print("3. sort a list by the length of the strings")
print("4. sort a list by the length of the strings and alphabetically")
print("5. sort a list by the length of the strings and alphabetically and reverse")
print("6. sort a list by the length of the strings and alphabetically and reverse and print")
print("7. exit")
while True:
    x = int(input("please choose an option"))
    if x == 1:
        sort()
    elif x == 2:
        sort_list_by_yourself()
    elif x == 3:
        sort_list_by_length()
    elif x == 4:
        sort_list_by_length_and_alphabetically()
    elif x == 5:
        sort_list_by_length_and_alphabetically_and_reverse()
    elif x == 6:
        sort_list_by_length_and_alphabetically_and_reverse_and_print()
    elif x == 7:
        break
    else:
        print("invalid option")