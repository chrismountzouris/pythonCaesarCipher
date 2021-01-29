def encrypt(message, key):

    encrypted_message = ''

    for letter in message:

        if (letter.isalpha() == True):

            if (letter.isupper() == False):

                letter_position_in_alphabet = ord(letter) - 97

                print (letter_position_in_alphabet)

            else:

                letter_position_in_alphabet = ord(letter) - 65

            shift = (letter_position_in_alphabet + int(key)) % 26

            if (letter.isupper() == False):

                encrypted_message += chr(shift + 97)

            else:

                encrypted_message += chr(shift + 65)

        else:

            encrypted_message += letter

    print (encrypted_message)

    return encrypted_message


message = input ("Please enter a message to encrypt: ")

while True:
    
    key = input ("Please enter a encryption shift: ")

    # Under that condition included non numeric inputs.

    # Note that negative integers are signed with the character '-' so are consider as non numeric too.

    # Note that inputs with decimal digits are considered as non numeric because of the character of ','.
    
    if (key.isnumeric() == False):

        print ("Invalid input. Please enter a positive numeric value.")

    # Under that condition included only numeric inputs that are positive.
    
    else:

        break

encrypt(message, key)
