def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    n=int(s)
    while n>0:
        k+=n%10
        n=n//10
    return k