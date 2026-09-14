from random import randint

# Helper function to calculate max value
def max_number(nums_dict):
    """This function was created
    to help calculate the highest score 
    for the Adagrams game. 

    Since there are no negative scores,
    this function was implemented to accept 
    only numbers >= 0 (dictionary keys).
    
    Input: dictionary with scores as keys
    Output: the max key
    """

    if not nums_dict:
        return None

    max_num = 0

    for num in nums_dict:
        if num > max_num:
            max_num = num

    return max_num

# Wave 1
def draw_letters():

    letter_pool = {
        'A': 9, 
        'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2, 
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2, 
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1, 
        'Y': 2, 
        'Z': 1
    }

    hand = []
    n = 98

    while len(hand) < 10:
        random_num = randint(1, n)
        temp = 0

        for letter, count in letter_pool.items():
            temp += count

            if temp >= random_num:
                hand.append(letter)
                letter_pool[letter] -= 1
                n -= 1
                break

    return hand

# Wave 2
def uses_available_letters(word, letter_bank):

    hand = {}
    for letter in letter_bank:
        if letter not in hand:
            hand[letter] = 1
        else:
            hand[letter] += 1  

    for letter in word.upper():
        if letter not in hand:
            return False
        else:
            if hand[letter] == 0:
                return False
            hand[letter] -= 1  

    return True  

# Wave 3
def score_word(word):

    SCORE_DISTRIBUTION = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, 
        "N": 1, "R": 1, "S": 1, "T": 1, "D": 2, 
        "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10
    }

    score = 0

    for letter in word.upper():
        if letter in SCORE_DISTRIBUTION:
            score += SCORE_DISTRIBUTION[letter]

    if 6 < len(word) < 11:
        score += 8

    return score

# Wave 4
def get_highest_word_score(word_list):

    word_info = {}

    for word in word_list:
        score = score_word(word)
        if score not in word_info:
            word_info[score] = []
        word_info[score].append(word)

    highest_score = max_number(word_info)
    highest_score_list = word_info[highest_score]
    word_choice = ""

    # Check if there are no ties
    if len(highest_score_list) == 1:
        word_choice = highest_score_list[0]

    # There are ties otherwise
    else:
        min_length = len(highest_score_list[0])
        word_choice = highest_score_list[0]

        for word_name in highest_score_list:
            if len(word_name) == 10:
                word_choice = word_name
                break    
            else:  
                if len(word_name) < min_length:
                    min_length = len(word_name)
                    word_choice = word_name
            
    return (word_choice, highest_score)