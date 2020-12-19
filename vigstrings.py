# Given a string s and an alphabet a,
# shifts s by letter shift
def shift_by_letter(s, shift, a):
    shifted_s = ''
    for char in s:
        shifted_s += a[(a.index(char) - a.index(shift)) % len(a)]
    return shifted_s


# Given a string s and an alphabet a,
# shifts s by shift
def shift_by_number(s, shift, a):
    shifted_s = ''
    for character in s:
        shifted_s += a[(a.index(character) - shift) % len(a)]
    return shifted_s


# Given a string s and an alphabet a,
# shifts s by shift word
def shift_by_word(s, shift, a):
    shifted_s = ''
    for i in range(len(s)):
        shifted_s += shift_by_letter(s[i], shift[i % len(shift)], a)
    return shifted_s


# Given a string s,
# retuns every nth character in the string
# beginning at startindex
def every_nth_letter(s, n, startindex):
    s = s[startindex:]
    new_s = ''
    for i in range(len(s)):
        if (i + 1) % n == 0:
            new_s += s[i]
    return new_s


# Given a string s, splits the string into substrings of length length
# and returns these substrings as a list
def separate_string(s, length):
    substrings = []
    if length != 0:
        while s:
            if len(s[:length]) == length:
                substrings.append(s[:length])
                s = s[length:]
            else:
                break
    return substrings
