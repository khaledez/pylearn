def bubble_sort(list: iter) -> iter:
    local_list = list.copy()
    for i in range(len(local_list) - 1):
        for j in range(len(local_list[i+1:])):
            if local_list[i] > local_list[i+j]:
                tmp = local_list[i]
                local_list[i] = local_list[i+j]
                local_list[i+j] = tmp
            
    return local_list


print(bubble_sort([2, 8, 1, 7, 9, 3, 6, 4, 5, 10]))
