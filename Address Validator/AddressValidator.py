def addressVal(address):
    #strips the leading/trailing spaces, and converts the string to lowercase, then removes all spaces in the string
    address = address.strip().lower()
    #removes all spaces in the string
    address = address.replace(" ", "")
    dot = address.rfind(".") #finds the last occurrence of the '.' character in the string and returns its index
    at = address.find("@") #finds the first occurrence of the '@' character in the string and returns its index
    valid = True

    #if dot index is not found, return invalid
    if (dot == -1):
        print("Invalid - no '.' found")
        valid = False
    #if at index is not found, return invalid
    if (at == -1):
        print("Invalid - no '@' found")
        valid = False
    #if the dot is before the at, return invalid
    if (dot < at):
        print("'.' needs to be after '@'")
        valid = False
    #if the at is at the beginning of the string, return invalid
    if (at == 0):
        print("There must be text before the '@' symbol")
        valid = False
    #if the dot is at the end of the string, return invalid
    if (dot == len(address) - 1):
        print("There must be text after the '.' symbol")
        valid = False
    
    if (valid):
        print("Valid!")

print("This program will decide if your input is a valid email address")
while(True):
    print("A valid email address needs:")
    print("     1. an '@' symbol and a '.' symbol")
    print("     2. the '@' to be before the '.'")
    print("     3. text before the '@' and after the final '.'")
    print()
    x = input("Input your email address:")

    addressVal(x)
    print()
