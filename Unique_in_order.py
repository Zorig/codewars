def unique_in_order(iterable):
    arr = []
    last = None
    for i, v in enumerate(iterable):
        if v is not last:
            last = v
            arr.append(last)
    return arr
