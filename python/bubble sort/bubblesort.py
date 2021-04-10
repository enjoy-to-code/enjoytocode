int_array = [3, 5, 6, 8, 10, 12, 4]

def bubble_sort(sort_list):
    swapped = True

    # if list is ordered swapped will remain false en exit loop
    while(swapped):
        swapped = False
        for i in range(len(sort_list) - 1):
            if sort_list[i] > sort_list[i+1]:
                # Swap elements
                sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
                swapped = True
                print(sort_list)

bubble_sort(int_array)
print(int_array)







