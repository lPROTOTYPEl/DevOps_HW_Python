def fib(n):
    f, s = 1, 1
    res = [f, s]

    for i in range(n - 2):
        next_n = f + s
        f = s
        s = next_n
        res.append(next_n)

    return res

def main():
    fib_list = fib(12)
    print(" ".join(str(x) for x in fib_list))

if __name__=="__main__":
    main()
