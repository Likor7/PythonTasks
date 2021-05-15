def create_dict_first_method(name: str, age: int, hobby: str):
    return {"Name": name, "Age": age, "Hobby": hobby}


def create_dict_second_method(d: dict, name: str, age: int, hobby: str):
    return d.update({"Name": name, "Age": age, "Hobby": hobby})


def main():
    dictionary_first = create_dict_first_method("Denis", 26, "Books")
    print(dictionary_first, '\n')

    d = dict.fromkeys(["Name", "Age", "Hobby"])
    create_dict_second_method(d, "Denis", 26, "Books")
    print(d)


if __name__ == '__main__':
    main()
