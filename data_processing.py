import random

def compoundConsonants(letter):
    compound_r={"B","C","D","F","G","K","P","T","W"}
    compound_l={"B","C","F","G","L","P"}
    if random.randint(0,1)==0:
        for consonant in compound_r:
            if consonant==letter:
                letter += "R"
    if len(letter)==1:
        for consonant in compound_l:
            if consonant == letter:
                letter += "L"
    return letter


def centerUsername(length_username):
    spaces=str()
    if length_username<18:
        for i in range(18-length_username):
            spaces+=" "
    return spaces

def processUsername(var,length,username,consonants,vowels):
    start_consonant = 1 if var.get() == 1 else 0
    added_letters = int()
    cannot_add_u = False
    for i in range(length):
        is_consonant=(i + start_consonant) % 2
        if added_letters < length:
            if (is_consonant):
                missing_letters = (length-1) - added_letters
                if (missing_letters) > 1:
                    letter = random.choice(consonants)
                    if letter != "Q":
                        single_consonants = bool(random.randint(0, 1))
                        if single_consonants == False:
                            letter = compoundConsonants(letter)
                    else:
                        letter += "U"
                        cannot_add_u = True

                        print(str(added_letters))
                else:
                    letter = random.choice("BCDFGHJKLMNPRSTVWXYZ")
                username += letter
            else:
                if cannot_add_u == True:
                    letter = random.choice("AEIO")
                    cannot_add_u = False
                else:
                    letter = random.choice(vowels)
                username += letter
        added_letters = len(username)
    return username
