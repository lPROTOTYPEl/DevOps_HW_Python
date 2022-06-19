import re

def get_nums_from_string(string):
    # Находим все подстроки, начинающиеся с -, + или пустого значения,
    # а затем идет последовательность из цифр
    nums = re.findall(r'[-+]?\d+', string)
    # Переводим все элементы списка в числа
    nums = [int(i) for i in nums]

    return nums

def count_sum(num_list):
    sum = 0

    for element in num_list:
        sum += element

    return sum

def main():
    string = input()
    num_list = get_nums_from_string(string)
    print(count_sum(num_list))

if  __name__=="__main__":
    main()
