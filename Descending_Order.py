def Descending_Order(num):
    # Bust a move right here
    num_list = []
    for index in range(len(str(num))):
        num_list.append(str(num)[index])

    sorted_list = sorted(num_list, reverse=True)
    sorted_string = ''.join(sorted_list)

    return int(sorted_string)
