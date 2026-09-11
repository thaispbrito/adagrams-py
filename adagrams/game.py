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

    hand = {}
    for letter in letter_bank:
        if letter not in hand:
            hand[letter] = 1
        else:
            hand[letter] += 1  

    word_upper = word.upper()
    word_count = {}         
    for char in word_upper:
        if char not in letter_bank:
            return False
        else:
            if char not in word_count:
                word_count[char] = 1
            else:
                word_count[char] += 1 

    for item in word_count:
        if word_count[item] > hand[item]:
            return False    

    return True  

def score_word(word):

    SCORE_DISTRIBUTION = [
        [1, ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T")],
        [2, ("D", "G")],
        [3, ("B", "C", "M", "P")],
        [4, ("F", "H", "V", "W", "Y")],
        [5, ("K")],
        [8, ("J", "X")],
        [10, ("Q", "Z")]
    ]

    score = 0

    word_upper = word.upper()

    for char in word_upper:

        for i in range(7):

            if char in SCORE_DISTRIBUTION[i][1]:
                score += SCORE_DISTRIBUTION[i][0]

    if 6 < len(word) < 11:
        score += 8

    return score

def get_highest_word_score(word_list):

    highest_score = 0

    word_scores = []
    word_names = []
    word_lengths = []

    word_scores_ties = []
    word_names_ties = []
    word_lengths_ties = []


    for word in word_list:

        score = score_word(word)
        word_names.append(word)
        word_scores.append(score)
        word_lengths.append(len(word))

    # Computing the highest score among the words

    if len(word_scores) == len(set(word_scores)):

        highest_score = max_number(word_scores)

        for i in range(len(word_list)):
            highest_score = max_number(word_scores)

            if word_scores[i] == highest_score:

                word = word_names[i]
    else:

        max_score = max_number(word_scores)

        for i in range(len(word_list)):

            if word_scores[i] == max_score:
                word_names_ties.append(word_names[i])
                word_scores_ties.append(word_scores[i])
                word_lengths_ties.append(word_lengths[i])


        if 10 in word_lengths_ties:
            for i in range(len(word_names_ties)):
                if word_lengths_ties[i] == 10:
                    word = word_names_ties[i]
                    highest_score = max_score
                    break

        else:
            min_length = min_number(word_lengths_ties)

            for i in range(len(word_names_ties)):
                if word_lengths_ties[i] == min_length:
                    word = word_names_ties[i]
                    highest_score = max_score

    return (word, highest_score)

# Helper function to calculate max
def max_number(nums):

    if not nums:
        return None

    max_num = nums[0]

    for n in nums:
        if n > max_num:
            max_num = n

    return max_num

# Helper function to calculate min
def min_number(nums):

    if not nums:
        return None

    min_num = nums[0]

    for n in nums:
        if n < min_num:
            min_num = n

    return min_num