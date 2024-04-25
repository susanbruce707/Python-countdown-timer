# integer input function
def int_input():
    try:
        x = int(input("Enter integer "))
    except ValueError:
        print("Only integers as input please")
        x = 0
        x = int_input()
    return x
    


q = int_input()
print(q)
