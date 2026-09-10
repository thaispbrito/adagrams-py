from random import randint

def draw_letters():

    letters = [
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", 
        "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
        "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", 
        "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", 
        "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", 
        "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", 
        "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"
    ]

    hand = []
    n = 98

    while len(hand) < 10:

        random_num = randint(1, n)
        index = random_num - 1

        hand.append(letters[index])
        letters.remove(letters[index])
        n -= 1

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass