
# Exception handling in python
# Case1
# Try : Block will hold the code which is excepted to execution error
try:
    a = int(input("Enter the num 1: "))
    b = int(input("Enter the num 2: "))
# Try : Block will catch the error and print a meaningful error
# Or perform correction required
except:
    print("Error: Please enter integer only")
# Else: Block will hold the code which needs to be executed
else:
    # Add Numbers
    c = a + b
    print("Sum = ", c)
# Finally: Finally is an optional block, it will execute in case of error or no error
finally:
    print("Thank you !, Execution Completed")


def inputlist():
    try:
        ln = int(input("Enter the length of the list : "))
        x = 0
        l = []
        while x < ln:
            # To get an ValueError enter element of the list other than integer example: float or character
            # Error = Please enter integers only
            y = int(input("Enter the element in the list : "))
            l.append(y)
            x = x + 1

        # Without error
        # z = 0
        # while z < ln:
        #     print(l[z], end=' ')
        #     z = z + 1
        # print()

        # Error = index is out of range
        # while x <= ln:
        #     print(l[x])

        # Error = unknown error
        # while z < ln:
        #     print(l[z])
        #     z = z + 1

    except ValueError:
        print("Error: Please enter integers only")
    except IndexError:
        print("Error: Please note that index is out of range")
    except:
        print("Error: There are an unknown error")
    else:
        return(l)
    finally:
        print("Thank you !, Execution Completed")

l1 = inputlist()
print(l1)