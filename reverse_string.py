#Code for reversing a string with recursion.

def reverse_string(s: str, n=0)->str:
    
    if len(s)==0:
        return ''
    else:
        n = len(s)
        return s[-1] + reverse_string(s[0:-1], n)

s = "pots&pans"

print(reverse_string(s))