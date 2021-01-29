def decrypt(message):

    x = range(26)

    for key in x:

        decrypted_message = ''

        for letter in message:

            if (letter.isalpha() == True):

                if (letter.isupper() == False):

                    letter_position_in_alphabet = ord(letter) - 97

                else:

                    letter_position_in_alphabet = ord(letter) - 65

                shift = (letter_position_in_alphabet - int(key)) % 26

                if (letter.isupper() == False):

                    decrypted_message += chr(shift + 97)

                else:

                    decrypted_message += chr(shift + 65)

            else:

                decrypted_message += letter

        print ("The decrypted message is:",decrypted_message,"for key:",key)

    return decrypted_message


message = input ("Please enter a message to decrypt: ")

decrypted_message = decrypt(message)
