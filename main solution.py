
import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
game_is_on=True
while game_is_on:
    try:
        nato_dict={row.letter: row.code for (index, row) in nato.iterrows()}

        user_word=input("Enter a word: ").upper()
        a=[nato_dict[i] for i in user_word]
        print(a)
        game_is_on=False
    except KeyError:
        print("Sorry, only letter in the alphabet please.")