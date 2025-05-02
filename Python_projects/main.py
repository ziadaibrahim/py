from Day1_functions import *
from Day2_functions import *
from Day3_function import check
############################## day 1 ##############################
#vowels
x = input("Enter your text: ")
print(vowels_count(x))

#location of i
text = input("Enter your text: ")
print(i_location(text))

#table of number
x = int(input("Enter the number: "))
table(x)

#mario1
x = int(input("Enter the pyramid height: "))
Mario1(x)


############################## day 2 ##############################
# sort 5 numbers
sort_numbers()

#nubmer multiplication
x = int(input("Enter the number: "))
result = generate_multiplication(x)
print(result)

#mario2
x=int(input("enter mario2 highiet"))
mario2(x)

#check name and email
uname = get_valid_name()
uemail = get_valid_email()
print(f"name is {uname}\nemail is {uemail}")

############################## day 3 ##############################
#check authentication
username = input("enter your name: ")
password = input("enter your pass: ")

if check(username, password):
    print("welcome")
else:
    print("invalid username or password")