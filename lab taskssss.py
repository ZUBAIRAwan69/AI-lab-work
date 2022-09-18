"""Task 1
"""
"""
num = 987654321
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
"""

"""Task 2
"""
"""
maximum = int(input(" Please Enter the Maximum Value : "))
even_total = 0
odd_total = 0
 
for number in range(1, maximum + 1):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
 
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, even_total))
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, odd_total))
"""

""" task3
"""

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
