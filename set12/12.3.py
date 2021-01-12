def mediana_sort(L, left, right):
    if not isinstance(left, int) or not isinstance(right, int) or left < 0 or right < 0:
        raise ValueError("Indexes must be positive integers!")
    if right < left:
        raise Exception("Right index can not be lower than the left index")
    L.sort()
    if len(L) % 2 == 1:
        return L[(right-left)//2]
    tmp = (right-left-1)//2
    return (L[tmp]+L[tmp+1])/2


L = [5, 4, 8, 7, 3]
print(mediana_sort(L, 0, len(L)))       # returns 5
L.append(2)
print(mediana_sort(L, 0, len(L)))       # returns 4.5