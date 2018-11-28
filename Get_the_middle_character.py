def get_middle(s):
    # your code here
    return s[(int(len(s)/2))] if not len(s) % 2 == 0\
        else s[int(len(s)/2)-1]+s[int(len(s)/2)]
