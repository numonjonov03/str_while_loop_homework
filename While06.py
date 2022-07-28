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
        if  s[i].isalpha() and (s[i]!="a" and s[i]!="u" and s[i]!="e" and s[i]!="i" and s[i]!="o" and s[i]!="o'" and s[i]!="A" and s[i]!="U" and s[i]!="E" and s[i]!="I" and s[i]!="O" and s[i]!="O'"):
            k+=1
        i+=1
    return k
print(main("codeschooluz"))