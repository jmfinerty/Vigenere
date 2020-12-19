from vigstrings import shift_by_letter


# Given a string s, an alphabet a,
# and the frequency with which a's letters occur in its language,
# return the variance v of s.
def variance(s, a, freqs):
    v = 0
    for i in a:
        observed_freq = s.count(i) / len(s)
        expected_freq = freqs[a.index(i)]
        v += ((observed_freq - expected_freq) ** 2) / expected_freq
    return v


# Given a string s,
# returns the IOC using formula from:
# http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/
def IOC(s):
    sum = 0
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = s.count(letter)
        sum += count * (count - 1)
    return (sum / (len(s) * (len(s) - 1)))


# Given a string s, an alphabet a,
# and the frequency with which a's letters occur in its language,
# Applies frequency analysis to determine the letter in a
# that s was most likely shifted by
def FA(s, a, freqs):
    # For every letter in English, shift s by this letter.
    # Determine for each shifted text how close
    # the distribution of letters is to English.
    # Choose the letter which produces the shift closest to English.
    shifts = []
    for letter in a:
        shifted_s = shift_by_letter(s, letter, a)
        v = variance(shifted_s, a, freqs)
        shifts.append((letter, v))
    shifts.sort(key=lambda x: x[1])
    return shifts[0][0]
