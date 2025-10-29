

#Initial input
operation = int(input("What operation would you like to do? (1 - Decimal to binary | 2 - Decimal to hexadecimal): "))

#############Decimal to Binary#############
def get_number_binary(dec_bin):

    bits_in_reverse = []

    if dec_bin == 0:
        return [0]

    while dec_bin > 0:
        last_bit = dec_bin % 2

        bits_in_reverse.append(last_bit)

        dec_bin = dec_bin // 2
    bits_in_reverse.reverse()

    return bits_in_reverse


#############Decimal to Hexadecimal#############
def get_number_hexa(dec_hex):
    hexa_key = "0123456789ABCDEF"
    nibbles_in_reverse = []

    if dec_hex == 0:
        return[0]


    while dec_hex > 0:
        last_nibble = dec_hex % 16
        hexa_conversion = hexa_key[last_nibble]
        nibbles_in_reverse.append(hexa_conversion)

        dec_hex = dec_hex // 16

    nibbles_in_reverse.reverse()

    return nibbles_in_reverse



#Processing
if operation <=0 or operation > 2:
    print("Not a valid option, try again.")


if operation == 1:
    user_decimal = int(input("Enter a integer decimal number to convert to binary: "))
    bit_list = get_number_binary(user_decimal)

    print(f"The number you choose was {user_decimal}")
    print(f"Your number in binary is: {bit_list}")

if operation == 2:
    user_decimal2 = int(input("Enter a integer decimal number to convert to hexadecimal: "))
    nibble_list = get_number_hexa(user_decimal2)
    hexa_string = ''.join(nibble_list)

    print(f"The number you chose was {user_decimal2}")
    print(f"Your number to hexadecimal is: {hexa_string)") 














