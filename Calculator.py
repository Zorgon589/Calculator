# Create Functions
def multiply(mylist):
    result = 1
    for x in mylist:
        result = result * x
    return result


def divide(mylist):
    result = mylist[0]
    for x in mylist[1:]:
        result = result / x
    return result


def add(mylist):
    result = 0
    for x in mylist:
        result = result + x
    return result


def subtract(mylist):
    result = mylist[0]
    for x in mylist[1:]:
        result = result - x
    return result


# Get Input
Calculate = True
A = True
while Calculate is True:
    A = True
    query = input("Please enter query: ")
# Identify method and solve
    # Multiplication
    if "*" in query:
        query_list_mul = query.split("*")
        multi = [float(x) for x in query_list_mul]
        answer = multiply(multi)
        print("The Multiplication of " + query + " is " + str(answer))
        while A is True:
            calculator = input("Please enter 'New' for new query or enter 'Quit' to exit program: ")
            if calculator.upper() == "NEW":
                A = False
                continue
            elif calculator.upper() == "QUIT":
                A = False
                Calculate = False
            else:
                print("Invalid Entry.")
    # Division
    elif "/" in query:
        query_list_div = query.split("/")
        division = [float(x) for x in query_list_div]
        answer = divide(division)
        print("The Division of " + query + " is " + str(answer))
        while A is True:
            calculator = input("Please enter 'New' for new query or enter 'Quit' to exit program: ")
            if calculator.upper() == "NEW":
                A = False
                continue
            elif calculator.upper() == "QUIT":
                A = False
                Calculate = False
            else:
                print("Invalid Entry.")
    # Addition
    elif "+" in query:
        query_list_add = query.split("+")
        addition = [float(x) for x in query_list_add]
        answer = add(addition)
        print("The Addition of " + query + " is " + str(answer))
        while A is True:
            calculator = input("Please enter 'New' for new query or enter 'Quit' to exit program: ")
            if calculator.upper() == "NEW":
                A = False
                continue
            elif calculator.upper() == "QUIT":
                A = False
                Calculate = False
            else:
                print("Invalid Entry.")
    # Subtraction
    elif "-" in query:
        query_list_sub = query.split("-")
        subtraction = [float(x) for x in query_list_sub]
        answer = subtract(subtraction)
        print("The Subtraction of " + query + " is " + str(answer))
        while A is True:
            calculator = input("Please enter 'New' for new query or enter 'Quit' to exit program: ")
            if calculator.upper() == "NEW":
                A = False
                continue
            elif calculator.upper() == "QUIT":
                A = False
                Calculate = False
            else:
                print("Invalid Entry.")
    # Invalid Input
    else:
        while A is True:
            calculator = input("Invalid query. Please enter 'New' to try again or enter 'Quit' to exit program:")
            if calculator.upper() == "NEW":
                A = False
                continue
            elif calculator.upper() == "QUIT":
                A = False
                Calculate = False
            else:
                print("Invalid Entry.")
