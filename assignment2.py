# # Largest Of Three Numbers
# a = 10
# b = 20
# c = 30

# if a >= b and a >= c:
#     print("Largest number is:", a)
# elif b >= a and b >= c:
#     print("Largest number is:", b)
# else:
#     print("Largest number is:", c)

# s = input("Enter a string: ")

# if s.startswith("x"):
#     s = s[1:]

# elif s.endswith("x"):
#     s = s[:-1]

# print("Modified string:", s)

s = input("Enter string: ")
n = int(input("Enter n: "))
if n == 0:
    print("")
else:
    print(s[-n:] * n)

