
print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

lower_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']


def caesar(encode_or_decode, input_text, shift_amount):
    output_text = ""
    for letter in input_text:
        if letter in lower_alphabet:
            start = lower_alphabet.index(letter)
            if encode_or_decode == "encode":
                new_position = start + shift_amount
            else:
                new_position = start - shift_amount
            cypher_letter = lower_alphabet[new_position]
            output_text += str(cypher_letter)
        elif letter in upper_alphabet:
            start = upper_alphabet.index(letter)
            if encode_or_decode == "encode":
                new_position = start + shift_amount
            else:
                new_position = start - shift_amount
            cypher_letter = upper_alphabet[new_position]
            output_text += str(cypher_letter)
        else:
            output_text += str(letter)
    print(f"The encoded text is: \n{output_text}\n")


def repeat():
    encrypt_decrypt = input("\nType 'encode' to encrypt, or 'decode' to decrypt:\n").lower()

    def script(direction):
        if direction == "encode":
            text = input("Type your message:\n")
            pre_shift = int(input("How far do you want to shift the message?:\n"))
            shift = pre_shift % 26
            caesar(direction, text, shift)
            again = input("Would you like to go again?\n").lower()
            if again == "y" or again == "yes":
                repeat()
            else:
                print("Have a great day! :)")

        elif direction == "decode":
            text = input("What message would you like to decode?:\n")
            pre_shift = int(input("How far is the shift?:\n"))
            shift = pre_shift % 26
            caesar(direction, text, shift)
            again = input("Would you like to go again?\n").lower()
            if again == "y" or again == "yes":
                repeat()
            else:
                print("\nHave a great day! :)")

        else:
            direction = input("I did not understand that. Did you want to encode or decode?\n")
            if direction == "encode":
                script(direction)
            elif direction == "decode":
                script(direction)
    script(encrypt_decrypt)


repeat()
