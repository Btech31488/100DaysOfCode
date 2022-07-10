
PLACEHOLDER = "[name]"


with  open(r"./Input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()
    

with open(r"./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
       striped_name = name.strip()
       new_letter = letter_contents.replace(PLACEHOLDER, striped_name)
       with open(fr"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)



