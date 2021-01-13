def mediana_sort(L, left, right):
    if not isinstance(left, int) or not isinstance(right, int) or left < 0 or right < 0:
        raise ValueError("Indexes must be positive integers!")
    if right < left:
        raise Exception("Right index can not be lower than the left index")
    sortedL = sorted(L[left:right])
    if len(sortedL) % 2 == 1:
        return sortedL[(len(sortedL))//2]
    tmp = (len(sortedL)-1)//2
    return (sortedL[tmp]+sortedL[tmp+1])/2


L = [5, 4, 8, 7, 3]
print(mediana_sort(L, 0, len(L)))       # returns 5
L.append(2)
print(mediana_sort(L, 0, len(L)))       # returns 4.5