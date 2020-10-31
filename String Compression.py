"""Problem
    Given a string in the form "AAABBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4".
    For this problem, you can falsely "compress" strings of single or double letters. For
    instance , it is okay for "AAB" to return "A2B1" even though this technically take more
    spaces.
    the Function should also be case sensitive, so that a string "AAAaaa" returns "A3a3"
    """

"""Solution
    Since python strings are immutable, we'll need to work off of a list of
    characters, and at the end convert that list back into a string with a join
    statement.
    
    Time and space complexity of O(n)"""
"""Run length compression algorithm"""

def compress(s):

    r = ""
    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s+"1"

    last = s[0]
    cnt = 1
    i = 1
    while i < l:
        if s[i] == s[i-1]:
            cnt+=1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1



        i += 1


    r = r + s[i-1] + str(cnt)


    return r

print(compress("AABBBSSSSttt"))




