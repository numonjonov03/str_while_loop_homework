def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    i=0
    while len(s)>i:
        if s[i].isdigit() and int(s[i])%2==1:
            k+=1
        i+=1
    return k