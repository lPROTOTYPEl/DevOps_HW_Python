def get_dict(string):
    # Cписок всех слов строки
    w_list = string.split(' ')
    # Список уникальных слов строки
    w_set = set(w_list)

    w_dict = {}
    # Счетчтик максимального количества повторений слова в строке
    max_count = 0

    for word in w_set:
        count = w_list.count(word)

        if count > max_count:
            max_count = count

        w_dict.update({word:count})

    return (w_dict, max_count)

def print_result(w_dict, max_count):
    for w, c in w_dict.items():
        if c == max_count:
            print("{0} - {1}".format(c, w))

def main():
    string = input("Enter text: ")
    # спомощью casefold() игнорируем регистр
    w_dict, max_count = get_dict(string.casefold())
    print_result(w_dict, max_count)

if __name__=="__main__":
    main()
