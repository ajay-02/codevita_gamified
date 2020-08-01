def palindrome(s,x):
    l=len(s)
    if(x<0):
        x+=l
    for i in range(0,l//2):
        if(s[(i+x)%l]!=s[((l-i-1+x)%l)]):
            return False
    return True
def finds(s):
    for i in range(0,len(s)):
        if(palindrome(s,i) or palindrome(s,-i)):
            return i
    return -1
for _ in range(int(input())):
    print(finds(input()))
