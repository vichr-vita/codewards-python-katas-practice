

def rot13(message: str) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET_POS = {n[1]: n[0] for n in zip(range(26), ALPHABET)}
    SHIFTER = 13
    s = ''
    for ch in message:
        if not ch.lower() in ALPHABET:
            s += ch
            continue
        wasupper = ch.isupper()
        new_pos = (ALPHABET_POS[ch.lower()] + SHIFTER) % 26
        new_letter = ALPHABET[new_pos]
        s += new_letter if not wasupper else new_letter.upper()
    return s
