import pandas

nato_alph_dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:
nato_alphabet = {rows.letter: rows.code for (index, rows) in nato_alph_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
encode_decode = input("Encode or Decode?  ").lower()
if encode_decode == 'encode':
    word_input = input("Enter a word:  ").upper()
    letters_list = list(word_input)
    coded_letters_list = [nato_alphabet[letter] for letter in letters_list]
    print(*coded_letters_list)
elif encode_decode == 'decode':
    code_input = input("Type in the encoded message with spaces between each word:  ").title()
    code_list = code_input.split()
    decoded_letters_list = [list(nato_alphabet.keys())[list(nato_alphabet.values()).index(word)] for word in code_list]
    print(*decoded_letters_list)
