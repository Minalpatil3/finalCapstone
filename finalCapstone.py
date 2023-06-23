#Cypher is going to use the 15th letter after the letter you want to use.
#Create a function encode_message that will encode any message you give it.


def encode_message(message):
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                encoded_message += chr((ord(letter) + 15 - 65) % 26 + 65)
            else:
                encoded_message += chr((ord(letter) + 15 - 97) % 26 + 97)
        else:
            encoded_message += letter
    print(encoded_message)

encode_message("Hello World! This is a compulsory task for Cypher.")
