def alphabet_position(letter):
    count = 0
    while count < 26:
        for x in alphabet:
            if letter.lower() == x:
                return count
            else:
                count += 1

def count_key(phrase):
    key_list = []
    for l in phrase:
        count = 0
        if l.isalpha():
            for x in alphabet:
                if l == x:
                    key_list.append(count)
                else:
                    count += 1
        else:
            key_list = [int(x) for x in phrase]
    print(key_list)
    return key_list

alphabet = [
'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z'
]
