from helpers import alphabet_position, alphabet

def encrypt(bullshit, rot):

    new_word = []
    for x in bullshit:
        if x.isalpha() and x.islower():
            if alphabet_position(x)+int(rot) < 26:
                new_position = alphabet_position(x)+int(rot)

            else:
                new_position = (alphabet_position(x)+int(rot))-26
            aleph = alphabet[new_position]
            new_word.append(aleph)

        elif x.isalpha() and x.isupper():
            if alphabet_position(x)+int(rot) < 26:
                new_position = alphabet_position(x)+int(rot)
            else:
                new_position = (alphabet_position(x)+int(rot))-26
            aleph = alphabet[new_position].upper()
            new_word.append(aleph)
        else:
            new_word.append(x)

    print("".join(new_word))
    return("".join(new_word))

def main():
    encrypt(input("What phrase?\n"), input("Rotate?\n"))

if __name__ == '__main__':
    main()
    # alphabet_position(input("What letter?"))
    # encrypt(input("What phrase?\n"), input("Rotate?\n"))
