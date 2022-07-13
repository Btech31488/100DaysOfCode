import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_letters_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_letter_dict = {row.letter:row.code for (index, row) in nato_letters_frame.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
split_word = [nato_letter_dict[letter] for letter in word]
print(split_word)