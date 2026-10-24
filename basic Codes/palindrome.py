num = int(input("Enter number:"))
rev = 0
n = num
while(n>0):
    rev = rev*10 + (n%10)
    n = n//10
if (num == sum):
    print("Palindrome Number")
else:
    print("Not Palindrome")