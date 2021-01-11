# Poprawić wybrany algorytm sortowania, aby przyjmował jako dodatkowy argument funkcję porównującą elementy na liście 

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

cmp = lambda x, y: (x > y) - (x < y)

def selectsort(L, left, right, cmpfunc=cmp):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if cmpfunc(L[j], L[k]) < 0:
                k = j
        swap(L, i, k)

if __name__ == "__main__":
    example_list = [8, 7, 5, 2, 4, 15, 6]
    # sortowanie w odwrotnej kolejności
    selectsort(example_list, 0, 6, cmpfunc=lambda x, y: -cmp(x, y))
    print(example_list)