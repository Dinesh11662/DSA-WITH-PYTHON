n =int(input("Enter the Number"))
rev=0
while n>0:
    rev=(rev*10 )+ ( n%10)
    n=n//10
print(f"Reverse Number =",rev)