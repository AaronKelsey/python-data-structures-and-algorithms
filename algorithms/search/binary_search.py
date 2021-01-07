def binary_search(sorted_list, item, low=0, high=None):
    if len(sorted_list) == 0:
        return False
    else:
        if high is None:
            high = len(sorted_list) - 1

        while low <= high:
            mid_point = (low + high) // 2

            if sorted_list[mid_point] == item:
                return True
            elif sorted_list[mid_point] < item:
                low = mid_point + 1
            elif sorted_list[mid_point] > item:
                high = mid_point - 1
    return False


if __name__ == '__main__':
    array = []
    for i in range(0, 100):
        array.append(i + 1)

    target_number = 777777
    print(f'Target number: {target_number}')

    found = binary_search(array, target_number, 0, len(array) - 1)
    print(found)
