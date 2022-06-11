def is_even(num):
    if num%2!=0:
        return False
    return True
def power(num,n):
    ans=1
    for i in range(n):
        ans*=num
    return ans


