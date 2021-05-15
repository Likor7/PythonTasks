def get_value_from_list_first_method(data: list, index: int):
    try:
        return data[index]
    except IndexError:
        return "None"


def get_value_from_list_second_method(data: list, index: int):
    for i in range(len(data)):
        if i == index:
            return data[index]
    else:
        return "None"


def main():
    print(get_value_from_list_first_method([1, 2, 3], 1))
    print(get_value_from_list_first_method([1, 2, 3], 16), '\n')

    print(get_value_from_list_second_method([1, 2, 3], 1))
    print(get_value_from_list_second_method([1, 2, 3], 16))


if __name__ == '__main__':
    main()
