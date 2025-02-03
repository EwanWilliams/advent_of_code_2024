def get_lists():
    left_list = []
    right_list = []
    with open("input.txt", "r") as f:
        for row in f:
            left_list.append(int(row.split("   ")[0]))
            right_list.append(int(row.split("   ")[1]))
    
    return left_list, right_list


def get_total_distance(left, right):
    left.sort()
    right.sort()
    total_distance = 0

    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])
    
    return total_distance


if __name__ == "__main__":
    lists = get_lists()
    print(get_total_distance(lists[0], lists[1]))