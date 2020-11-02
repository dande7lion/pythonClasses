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
