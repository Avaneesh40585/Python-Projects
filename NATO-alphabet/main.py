import pandas
df=pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows():
# new_dict = {new_key:new_value for (index, row) in df.iterrows()}

nato_phonetic_alphabet={ row.letter:row.code for (index,row) in df.iterrows()}

check=1
while (check):
    try:
        user_input=input("Please enter a word:")
        key_list=[letter.upper() for letter in user_input]
        value_list=[ nato_phonetic_alphabet[key] for key in key_list]
    except KeyError:
        print("Sorry, please enter the letters from the alphabet only.")
    else:
        print(value_list)
        check=0