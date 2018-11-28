def find_short(s):
    # your code here
    s = s.split()
    low = len(s[0])
    for i in s:
        if low > len(i):
            low = len(i)
    return low  # l: shortest word length
