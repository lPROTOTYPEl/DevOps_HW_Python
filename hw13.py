def convert(t, celsius):
    if celsius:
        temp = to_celsius(t)
    else:
        temp = to_fahrenheit(t)

    return temp

def to_celsius(t):
    return (t - 32) * 5 / 9

def to_fahrenheit(t):
    return t * 1.8 + 32

def main():
    s1 = int(input("Enter Fahrenheit temp: "))
    s2 = int(input("Enter Celsius temp: "))
    t1 = convert(s1, True)
    t2 = convert(s2, False)

    print("{0} F = {1} C".format(s1,t1))
    print("{0} F = {1} C".format(t2,s2))

if __name__=="__main__":
    main()
