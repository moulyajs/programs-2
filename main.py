#write a program that takes the number of rows 'n' as input from the user and prints a number pattern in increasing ordervas shown below.if n is 5 ,the expected pattern is,
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15

"""n = int(input("Enter the number of rows: "))
num = 1
for i in range(1, n+1 ):
   for j in range(1,i+1):
       print(num, end=" ")
       num += 1
   print()"""
"""n = int(input('enter no of rows:'))
num = 1
for rows in range(1,n+1):
  for col in  range(1,rows+1):
    print(num,end=" ")
    num = num+1
  print()"""
# Write a program that takes the number of rows 'n' as input from the user and prints a diamond
 #pattern using asterisks (*) as shown in the sample example. Note that input ‘n’ will be an odd
# integer. The pattern should have a diamond shape with 'n' rows in the middle.If n is 5, the
#expected pattern is,
#    *
#   ***
#  *****
#   ***
#    *
"""n=int(input("Enter number of rows"))
if n%2==0:
 print("Enter an odd number please")
else:
 for i in range(1,n+1):
    spaces = abs(n//2-i+1)
    stars = n-2*spaces
    print(" "*spaces + "*"*stars)"""
"""n = int(input("enter a number"))
if n%2 == 0:
  print("pls enter odd number")

else:
  for i in range(1,n+1):
    spaces = abs(n//2-i+1)
    stars = n-2*spaces
    print(" "*spaces+"*"*stars)"""

#lcm of two number
"""m = int(input("enter a number:"))
n = int(input("enter a number:"))
if m<=0 and n <= 0:
  print("enter a positive number")
else:
  for i in range(1,m*n+1):
    if i % m ==0 and i%n == 0:
      lcm = i
      break

print("lcm of",m,"and",n,"is",lcm)"""

"""n = input("Enter a positive integer: ")
num = int(n)
if num <= 0:
 print("Please enter a positive integer.")
else:
 l = len(n)
 total = sum(int(digit) ** l for digit in n)
if total == num:
 print(f"{num} is an Armstrong number.")
else:
 print(f"{num} is not an Armstrong number.")"""

"""n = input("enter a positive integer:")
num = int(n)
if num <= 0:
  print("pls provide p number")
else:
  l = len(n)
  total = sum(int(digit)**l for digit in n)
  if total == num:
    print(f"{num} is an armstrong number")
  else:
    print(f"{num} is not an armstrong number")"""

"""Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user. Calculate and print the sum of the elements along both the main
diagonal (top-left to bottom-right) and the secondary diagonal (top-right to bottom-left) of the
2D list(nested list/ like matrix)."""
"""n = int(input("enter size of matrix"))
matrix=[]
for i in range(n):
  row = []
  for j in range(n):
    a = int(input("enter a number:"))
    row.append(a)
  matrix.append(row)
main_diagonal_sum = 0
secondary_diagonal_sum = 0
for i in range(n):
  main_diagonal_sum += matrix[i][i]
  secondary_diagonal_sum += matrix[i][n-1-i]
print(main_diagonal_sum)
print(secondary_diagonal_sum)"""
#Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
#integers from the user. Find and print the maximum value in the entire 2D list(nested list/ like
#matrix) along with its row and column indices
"""rows = int(input("enter rows"))
columns = int(input("enter columns"))
matrix = []
for i in range(rows):
  row = []
  for j in range(columns):
    a = int(input("enter a number:"))
    row.append(a)
  matrix.append(row)
max_value = None
max_row = -1
max_column = -1
for i in range(rows):
  for j in range(columns):
    if max_value is None or matrix[i][j] > max_value:
      max_value = matrix[i][j]
      max_row =i
      max_column = j

print(max_value)
print(max_row)
print(max_column)"""
## Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
##integers from the user. Find and print the minimum value in the entire matrix along with its
#row and column indices.
"""rows = int(input("enter rows"))
columns = int(input("enter columns"))
matrix = []
for i in range(rows):
  row = []
  for j in range(columns):
    a = int(input("enter a number:"))
    row.append(a)
  matrix.append(row)
min_value = None
min_row = -1
min_column = -1
for i in range(rows):
  for j in range(columns):
    if min_value is None or matrix[i][j] < min_value:
      min_value = matrix[i][j]
      min_row =i
      min_column = j

print(min_value)
print(min_row)
print(min_column)"""
"""str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if len(str1) == len(str2) and len(str1) > 0:
   combstr = str1 + str2
   if str2 in combstr:
       print('Y')
   else:
    print('N')
else:
 print('N')"""

"""str=input()
sub=list(set(str.split()))
sub.sort()
for i in sub:
 print(i)"""


"""str1 = input("Enter the first string: ").lower() 
str2 = input("Enter the second string: ").lower()
str1 = str1.replace(" ", "") 
str2 = str2.replace(" ", "")
if sorted(str1) == sorted(str2):
 print('Y')
else:
 print('N')"""

"""str1 = input("Enter a string: ")
str1 = str1.replace(" ", "").lower()
tot = 0
for c in str1:
   if 'a' <= c <= 'z':
    value = ord(c) - ord('a') + 1 
    tot += value
print(tot)"""

"""n = int(input("Enter the number of elements: "))
a = []
print('Enter the elemnts ')
for i in range(n):
 a.append(input())
k = int(input(f"Enter the desired occurrence frequency (k <= {n}): "))
if k > n:
 print("k should be less than or equal to n.")
b = []
for i in a :
 if (a.count(i)==k):
   b.append(i)
print(b)"""
"""
test_str = input("Enter the main string: ")
sub_str = input("Enter the substring to find: ")
words = test_str.split()
most_frequent_substring = ""
cmax = 0
for i in words:
    c = i.count(sub_str)
    if c > cmax:
        most_frequent_substring = i
        cmax = c
if most_frequent_substring:
 print("The most frequent substring is:", most_frequent_substring)
else:
 print("The substring was not found in any of the words.")"""

"""str1 = input("Enter a sentence: ")
str2 = ""
for c in str1:
      if 'a' <= c <= 'z':
          if c == 'z':
             str2 += 'a'
          else:
             str2 += chr(ord(c) + 1)
      elif 'A' <= c <= 'Z':
           if c == 'Z':
             str2 += 'A'
           else:
             str2 += chr(ord(c) + 1)
      else:
         str2 += c
print(str2)"""