def string_list_creation(string):
    c_word = ""
    f_list = []

    for word in string:
        if word != " ":
            c_word += word
        elif c_word not in f_list:
            f_list.append(c_word)
            c_word = ""
        else:
            c_word = ""

    return ' '.join(f_list)


def main():
    string = input("Enter text: ")
    print(string_list_creation(string))


if __name__ == "__main__":
    main()
