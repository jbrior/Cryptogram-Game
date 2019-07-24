import random
from phrases import Phrases

p_p = Phrases.phrases
p_a = Phrases.alpha
phrase_picked = 0
p_unique_letters = []
p_unique_nums = []
converted_phrase = ""

def get_rand_num():
    r = random.randint(1, 26)
    return r

def create_new_p():
    global converted_phrase
    for l in p_p[phrase_picked]:
        if l.lower() in p_unique_letters:
            temp_li = p_unique_letters.index(l.lower())
            temp_ni = p_unique_nums[temp_li] - 1
            converted_phrase = converted_phrase + p_a[temp_ni]
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

    print("\n" + converted_phrase.upper())

def run_game():
    for l in p_p[phrase_picked]:
        if l.lower() not in p_unique_letters and l.lower() in p_a:
            p_unique_letters.append(l.lower())

    p_len = len(p_unique_letters)

    while len(p_unique_nums) < p_len:
        r = get_rand_num()
        if r not in p_unique_nums:
            p_unique_nums.append(r)

    #print(str(p_unique_letters) + ":" + str(p_unique_nums))

    create_new_p()


run_game()