def binary_search(T: list, n: int, p: int):
    # n = len(T)
    real_T_postion = 0
    while T:
        pos = 0
        while pos < (n/2):
            if T[pos] == p:
                return real_T_postion
            else:
                pos += 1
                real_T_postion += 1
        n = n/2
        pos_remove = 0
        while pos_remove < pos:
            T.remove(T[0])
            pos_remove += 1
    return -1


Table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'w']
p = 'c'

print(binary_search(Table, len(Table), p))
