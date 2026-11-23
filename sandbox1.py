number = input("Enter an integer: ")
print("Your number:", number)
try:
    # block of code to try something goes here
    number = int(number)
except:
    # if anything goes wrong in the "try" part, then the script will run this block of code instead
    print("That's not a valid number integer. Please try again.")
    exit()

