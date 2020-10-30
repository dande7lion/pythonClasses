def prepare_rectangle(hight, width) -> str:
    rectangle_horizontal_edge = "+"
    rectangle_horizontal_space = "|"
    
    for i in range(width):
        rectangle_horizontal_edge += "---+"
        rectangle_horizontal_space += "   |"

    result = []

    line_numbers = hight*2+1 if hight is not 1 else 3
    for i in range(line_numbers):
        if i%2 == 0:
            result.append(rectangle_horizontal_edge)
        else:
            result.append(rectangle_horizontal_space)

    return "\n".join(result)

if __name__ == "__main__":
    hight = input("Enter rectangle's hight: ")
    width = input("Enter rectangle's width: ")
    try:
        hight = int(hight)
        width = int(width)
        if hight < 1 or width < 1:
            exit()
        print(prepare_rectangle(hight, width))
    except:
        print(f"{hight} and {width} are not a valid hight and width! Try again")
