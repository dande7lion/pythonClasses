def moda_py(L, left, right):
    if not isinstance(left, int) or not isinstance(right, int) or left < 0 or right < 0:
        raise ValueError("Indexes must be positive integers!")
    if right < left:
        raise Exception("Right index can not be lower than the left index")

    counter = dict()
    for element in range(left, right):
        counter[L[element]] = counter.get(L[element], 0) + 1
    maxCount = 0
    maxCountElement = 0
    for i in counter:
        if counter[i] > maxCount:
            maxCount = counter[i]
            maxCountElement = i
    return maxCountElement


L = [50, 8, 30, 54, 8, 50, 16, 65, 54, 50]
print(moda_py(L, 0, len(L)))        # returns 50
