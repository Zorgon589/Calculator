# Create Functions
# ["/","division"]
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


def format_list(operator):
    query_list = query.split(operator)
    Operations = [float(x) for x in query_list]
    return Operations


# Get Input
query = "NEW"
while query.upper() != "QUIT":
    query = input("Please enter query or type 'Quit' to exit: ")
# Identify method and solve

    # Multiplication
    if "*" in query:
        answer = multiply(format_list("*"))
        print("The Multiplication of " + query + " is " + str(answer))

    # Division
    elif "/" in query:
        answer = divide(format_list("/"))
        print("The Division of " + query + " is " + str(answer))

    # Addition
    elif "+" in query:
        answer = add(format_list("+"))
        print("The Addition of " + query + " is " + str(answer))

    # Subtraction
    elif "-" in query:
        answer = subtract(format_list("-"))
        print("The Subtraction of " + query + " is " + str(answer))

    # Quit
    elif query.upper() == "QUIT":
        break

    # Invalid Input
    else:
        query = input("Invalid query. Please enter 'New' to try again or enter 'Quit' to exit program:")
