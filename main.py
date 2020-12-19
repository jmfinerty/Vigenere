from vigstrings import shift_by_word
from vigkey import find_key


def main():

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # alphabet frequencies from:
    # https://en.wikipedia.org/wiki/Letter_frequency
    freqs = [.08167, .01492,
             .0202, .04253,
             .012702, .02228,
             .02015, .06094,
             .06966, .00153,
             .01292, .04025,
             .02406, .06749,
             .07507, .01929,
             .00095, .05987,
             .06327, .09356,
             .02758, .00978,
             .02560, .00150,
             .01994, .00077]

    ciphertext = open('ciphertext', 'r').read()
    key = find_key(ciphertext, alphabet, freqs)
    plaintext = shift_by_word(ciphertext, key, alphabet)

    print("\nEncrypted Text: ", ciphertext, '\n')
    print("Key: ", key, '\n')
    print("Decrypted Text: ", plaintext, '\n')


main()
