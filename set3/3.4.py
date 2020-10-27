while 1:
    input_value = input("Give a number: ")
    if input_value == "stop":
        break
    try:
        input_value = float(input_value)
        print (f"Number: {str(input_value)}, third power: {pow(input_value, 3)}")
    except:
        print (f"{input_value} is not a real number. Try again.")
