
# todo: Create a letter using starting_letter.txt for each name in invited_names.txt
# todo: Replace the [name] placeholder with the actual name.
# todo: Save the letters in the folder "ReadyToSend".
    
# * Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp

# * Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp

# * Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()
    
for name in names:
    stripped_name=name.strip()
    with open("./Input/Letters/starting_letter.txt") as input_file:
        initial_content=input_file.read()
        final_content=initial_content.replace("[name]",stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",'w') as output_file:
            output_file.write(final_content)