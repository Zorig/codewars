def square_digits(num):
    l = []
    for i in str(num):
        l.append(str(int(i)*int(i)))
    return int("".join(l))
