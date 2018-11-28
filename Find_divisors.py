def divisors(integer):
    divis = []
    for i in range(2, integer):
        if(integer%i==0):
            divis.append(i)
    if len(divis) == 0:
        return str(integer) + ' is prime'
    return divis
