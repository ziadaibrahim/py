
#1-Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.
vowels = ['a', 'e', 'i', 'o', 'u']
def vowels_count(x):
    c = 0
    for i in x:
        if i in vowels:
            c += 1
    return c


# 2-Write a program that prints the locations of "i" character in any string you added.
def i_location(text):
    locations = []
    for i in range(len(text)):
        if text[i] == "i":
            locations.append(i)
    return locations

# 3-Write a program that generate a multiplication table from 1 to the number passed.
def table(x):
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print(f"{i} * {j} = {i * j}")

# 4-Write a program that build a Mario pyramid like below:
def Mario1(x):
    for i in range(1, x + 1):
        print(" " * (x - i) + "*" * i)

