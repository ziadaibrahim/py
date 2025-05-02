# Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display
def sort_numbers():
    numbers = []
    print("Enter 5 numbers:")
    for i in range(5):
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)

    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    
    print("\nOriginal:", numbers)
    print("Ascending:", ascending)
    print("Descending:", descending)


# Write a program that generate a multiplication table from 1 to the number passed.
def generate_multiplication(n):
    final_list = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1): 
            row.append(i * j)
        final_list.append(row)
    return final_list

# mario pyramid 2
def mario2(size):
    l1 = [" "] * size
    for i in range(1, size + 1):
        l1[-i] = "*"
        print("".join(l1))
    else:
        print(l1)

# Ask the user for his name then confirm that he has entered his name(not an empty
# string/integers). then proceed to ask him for his email and print all this data(Bonus) check if it is
# a valid email or not
def get_valid_name():
    uname = input("Please enter your name: ")
    while not uname.isalpha():
        uname = input("Please enter a valid name (letters only): ")
    return uname

def get_valid_email():
    while True:
        uemail = input("Please enter your email: ")
        
        if uemail[0] in ("@", "."):
            continue
        if "@" not in uemail or "." not in uemail:
            continue
        if ".." in uemail:
            continue
        if uemail.index("@") > uemail.index("."):
            continue
        if uemail.index("@") - uemail.index(".") == -1:
            continue
        if uemail.endswith(".") or uemail.endswith("..") or uemail.endswith(".com."):
            continue
        if uemail.count("@") != 1:
            continue
        
        return uemail
