from vigmath import IOC, FA
from vigstrings import every_nth_letter


# Given a string s representing ciphertext,
# returns what is the most likely length of
# that ciphertext's key using the IOC process
def key_length(s):
    # append to list: (value, average IOC produced by value)
    IOCs = []
    for length in range(2, 24):  # assignment required max length 24
        sum = 0.0
        for i in range(length):
            sum += IOC(every_nth_letter(s, length, i))
        IOCs.append((length, sum/length))

    # return first value of list item with highest average IOC
    # This means it is the most "english-like"
    IOCs.sort(key=lambda i: i[1])
    return IOCs[-1][0]


# Given a string s,
# an alphabet a, and the frequency with which
# a's letters occur in its language,
# finds the key for s via frequency analysis
def find_key(s, a, freqs):
    length = key_length(s)
    key = ''
    for i in range(1, length+1):
        analyze = every_nth_letter(s, length, i)
        key += FA(analyze, a, freqs)
    return key
