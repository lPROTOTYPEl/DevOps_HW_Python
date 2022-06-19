def collatz(num):
    count = 0

    while num != 1:
        count += 1
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num /= 2

    return count

def main():
    n = input("Enter num: ")
    s = int(n)
    print("You need",collatz(s),"steps")

if __name__ == "__main__":
    main()
