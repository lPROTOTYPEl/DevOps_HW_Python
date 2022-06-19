def palindrome_finder(string):
    if string == string[::-1]:
        return True
    return False

def main():
    sum = 0

    for i in range(1, 1000000):
        if palindrome_finder(str(i)) and palindrome_finder("{0:b}".format(i)):
            sum += i

    print("sum = {}".format(sum))

if __name__=="__main__":
    main()


# Результат суммы: 872187
