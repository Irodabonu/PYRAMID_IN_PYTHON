def just_tree(size):
    he = 4
    we = 1
    si = 0
    beg = 0
    re = 55
    h = 0
    w = 0
    mid = 3
    while(beg < size):
        while(h < he):
            while(si < re): 
                print(' ', end='')
                si += 1
            while(w < we):
                print("*", end='')
                w += 1
            we += 2
            re -= 1
            si = 0
            print('')
            h += 1
            w = 0
        he += 1
        beg += 1
        h = 0
def k_tree(w):
    he = 4
    we = 1
    si = 0
    beg = 0
    re = 45
    h = 0
    w = 0
    mid = 3
    while(beg < size):
        while(h < he):
            while(si < re): 
                print(' ', end='')
                si += 1
            while(w < we):
                print("*", end='')
                w += 1
            we += 2
            re -= 1
            si = 0
            print('')
            h += 1
            w = 0
        he += 1
        beg += 1
        h = 0
w = int(input("Enter size of tree\n"))
just_tree(w)
