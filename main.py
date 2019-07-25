# -------- MODULE IMPORTS --------
import random
# -------- CLASS IMPORTS --------
from phrases import Phrases

# -------- GLOBAL VARIABLES --------
p_p = Phrases.phrases
ref = Phrases.phrases[1]
p_a = Phrases.alpha
phrase_picked = 0
p_unique_letters = []
p_unique_nums = []
converted_phrase = ""

""" 
    THIS FUNCTION GENERATES A RANDOM NUMBER BETWEEN 1 & 26
    (NUMBER OF LETTERS IN THE ALPHABET)
"""
def get_rand_num():
    r = random.randint(1, 26)
    return r


"""
    THIS FUNCTION TAKES THE ORIGINAL PHRASE AND
    ITERATES OVER EVERY LETTER AND CHANGES IT TO
    A RANDOM LETTER BASED ON THE RANDOM NUMBER 
    THAT IS ASSIGNED IN THE 'RUN_PUZZLE' FUNCTION
"""
def create_new_p():
    global converted_phrase
    for l in p_p[phrase_picked]:
        if l.lower() in p_unique_letters:
            temp_li = p_unique_letters.index(l.lower())
            temp_ni = p_unique_nums[temp_li] - 1
            converted_phrase = converted_phrase + p_a[temp_ni]

        # IF THERE IS A SPECIAL CHARACTER IN THE PHRASE LIKE A PERIOD
        # OR COLON. THESE STATEMENTS WILL NOT CONVERT THE CHARACTER TO
        # A RANDOM CHARACTER

        elif l == '\'':
            converted_phrase = converted_phrase + "'"
        elif l == '\"':
            converted_phrase = converted_phrase + '"'
        elif l == ' ':
            converted_phrase = converted_phrase + ' '
        elif l == '.':
            converted_phrase = converted_phrase + '.'
        elif l == ',':
            converted_phrase = converted_phrase + ','
        elif l == ':':
            converted_phrase = converted_phrase + ':'
        elif l == '-':
            converted_phrase = converted_phrase + '-'

    """ 
        PRINTS OUT THE FINAL CONVERTED PHRASE TO THE CONSOLE
        ALONG WITH THE VERSES REFERENCE WHICH IS IN IT'S ORIGINAL
        SPELLING
    """
    print("\n" + converted_phrase.upper() + "\n\n" + ref)


"""
    THIS FUNCTION ITERATES OVER THE ORIGINAL PHRASE AND PUTS ONLY THE
    **DIFFERENT** CHARACTERS INTO A LIST. EACH CHARACTER IS THEN ASSIGNED
    A RANDOM NUMBER BETWEEN 1 & 26.
"""
def run_puzzle():
    for l in p_p[phrase_picked]:
        if l.lower() not in p_unique_letters and l.lower() in p_a:
            p_unique_letters.append(l.lower())

    p_len = len(p_unique_letters)

    while len(p_unique_nums) < p_len:
        r = get_rand_num()
        if r not in p_unique_nums:
            p_unique_nums.append(r)

    """ UNCOMENT BELOW LINE TO SEE A MORE CLEAR OUTPUT OF HOW
        THE LETTERS ARE ASSIGNED TO A RANDOM NUMBER
    """
    # print(str(p_unique_letters) + ":" + str(p_unique_nums))

    create_new_p()


# STARTS THE FIRST FUNCTION CALL OF THE PROGRAM
run_puzzle()
