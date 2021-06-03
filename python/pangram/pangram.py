def is_pangram(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in sentence.upper():
            return False
    return True
