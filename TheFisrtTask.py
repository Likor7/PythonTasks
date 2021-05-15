def compare_elements(a: list, b: set):
    if len(a) == len(b):
        return "List and Set is equal"
    return "List is bigger" if len(a) > len(b) else "Set is bigger"


def main():
    task_two_list = [x for x in range(1, 20, 2)]
    print(task_two_list)
    # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    task_three_list = task_two_list
    task_three_list.extend([1, 5, 13, 20])
    print(task_three_list)
    # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 1, 5, 13, 20]

    task_four_list = set(task_three_list)
    print(task_four_list)
    # {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20}

    print(compare_elements(task_three_list, task_four_list))


if __name__ == '__main__':
    main()
