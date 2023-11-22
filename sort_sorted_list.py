def merge_sorted_lists(list1, list2):
    merged_list = []
    left_idex = right_idex = 0

    while left_idex < len(list1) and right_idex < len(list2):
        if list1[left_idex] < list2[right_idex]:
            merged_list.append(list1[left_idex])
            left_idex += 1
        else:
            merged_list.append(list2[right_idex])
            right_idex += 1

    while left_idex < len(list1):
        merged_list.append(list1[left_idex])
        left_idex += 1

    while right_idex < len(list2):
        merged_list.append(list2[right_idex])
        right_idex += 1

    return merged_list

# Example usage:
list1 = [2, 4, 7, 9, 11, 14, 20]
list2 = [0, 5, 8, 13, 19]

result = merge_sorted_lists(list1, list2)

print(result)
