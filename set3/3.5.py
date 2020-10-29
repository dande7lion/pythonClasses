def prepare_ruler(size) -> (str, str):
    if size == 0:
        return "|", "0"
    ruler_top = "|...."
    ruler_bottom = "0"
    for i in range(size-1):
        ruler_bottom += "{:>5}".format(str(i+1))
        if i < size-2:
             ruler_top += "|...."
    return ruler_top + "|", ruler_bottom

if __name__ == "__main__":
    length = input("Give length of the ruler: ")
    try:
        length = int(length)
        ruler_top, ruler_bottom = prepare_ruler(length)
        print(ruler_top)
        print(ruler_bottom)
    except:
        print(f"{length} is not a valid length! Try again.")