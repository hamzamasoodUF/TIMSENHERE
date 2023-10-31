def encode(password):

    input_array = [int(char) for char in password]
    for i in range(len(input_array) - 1, -1, -1):
        new_digit = input_array[i] + 3
        input_array[i] = new_digit % 10
    result_string = ''.join(map(str, input_array))

    return result_string



'__main__' == '__name__'


def console():
    print("menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

__main__ = __name__

cat = 1
while cat == 1:
    console()
    menu_value = int(input("please enter an option"))
    if menu_value > 3 or menu_value < 1:
        print("incorrect input format. Please try again")
    else:
        if menu_value == 1:
            password = input("Please enter your password to encode: ")
            while len(password) !=8:
                print("incorrect format please try again")
                password = input("please enter oyur parrwrrod to encoede")
            turtle = encode(password)
            print("Your password has been encoded and stored!")
        if menu_value == 2:
            print("missing decode")
        if menu_value == 3:
            break