def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    k=0
    i=0
    while len(s)>i:
        if  s[i].isalpha() and (s[i]!="a" or s[i]!="u" or s[i]!="e" or s[i]!="i" or s[i]!="o" or s[i]!="o'" or s[i]!="A" or s[i]!="U" or s[i]!="E" or s[i]!="I" or s[i]!="O" or s[i]!="O'"):
            k+=1
        i+=1
    return k