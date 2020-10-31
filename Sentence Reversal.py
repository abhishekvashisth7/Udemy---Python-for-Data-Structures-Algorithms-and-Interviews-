'''Problem
    Given a string of words,reverse all the words.
    e.g.
    Input : 'This is the best'
    Output: 'best the is This'
    As part of this exercise you should remove all leading and trailing whitespace.So that 
    inputs such as:
    '    space here'   and   'space here        '
    both
    'here space'
    '''

'''SOlution:
    We can also use split() and reversed[]
    '''

def rev_word1(s):
    return " ".join(reversed(s.split()))

def rev_word2(s):
    return " ".join(s.split()[::-1])

def rev_word(s):

    words = []
    length = len(s)
    spaces = [" "]

    i = 0

    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])
            

        i += 1

    return " ".join(reversed(words))

print(rev_word("       hello john    how are you    "))