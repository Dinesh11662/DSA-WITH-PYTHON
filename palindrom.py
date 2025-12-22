n=121
num=n
reslt=0
while n>0:
    ld=num%10    # O(log10(n)) time complaxsity
    reslt=(reslt*10)+ld
    num=num//10

if reslt==n:
    print("palindreom")
else:
    print("this number is not palindrome")
    
   