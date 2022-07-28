def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    n=int(s)
    while n>0:
        if n%10%2==1:
            k+=n%10
        n=n//10
    return k