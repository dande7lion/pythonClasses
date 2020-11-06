# 3.5.py (unchanged from the last set)

def prepare_ruler(size) -> str:
    if size == 0:
        return "|\n" + "0"
    ruler_top = "|...."
    ruler_bottom = "0"
    for i in range(size-1):
        ruler_bottom += "{:>5}".format(str(i+1))
        if i < size-2:
             ruler_top += "|...."
    return ruler_top + "|\n" + ruler_bottom

if __name__ == "__main__":
    length = input("Give length of the ruler: ")
    try:
        length = int(length)
        if length < 0:
            exit()
        ruler = prepare_ruler(length)
        print(ruler)
    except:
        print(f"{length} is not a valid length! Try again.")

# 3.6.py (unchanged from the last set)

def prepare_rectangle(height, width) -> str:
    rectangle_horizontal_edge = "+"
    rectangle_horizontal_space = "|"
    
    for i in range(width):
        rectangle_horizontal_edge += "---+"
        rectangle_horizontal_space += "   |"

    result = []

    line_numbers = height*2+1 if height is not 1 else 3
    for i in range(line_numbers):
        if i%2 == 0:
            result.append(rectangle_horizontal_edge)
        else:
            result.append(rectangle_horizontal_space)

    return "\n".join(result)

if __name__ == "__main__":
    height = input("Enter rectangle's height: ")
    width = input("Enter rectangle's width: ")
    try:
        height = int(height)
        width = int(width)
        if height < 1 or width < 1:
            exit()
        print(prepare_rectangle(height, width))
    except:
        print(f"{height} and {width} are not a valid height and width! Try again")
