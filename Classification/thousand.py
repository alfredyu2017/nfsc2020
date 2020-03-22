def thousand (a, b):
    if (b-a) <999:
        if ((b-a)%2) == 0:
            c = (1000-(b-a))/2
            x, y = int(a-c), int(b+c)
        else:
            c = (999-(b-a))/2
            x, y = int(a-c), int(b+c+1)
    elif (b-a) == 999:
        x, y = int(a), int(b+1)
    else:
        if ((b-a)%2) == 0:
            c = ((b-a)-1000)/2
            x, y = int(a+c), int(b-c)
        else:
            c = ((b-a)-999)/2
            x, y = int(a+c), int(b-c+1)
    return x, y
