
# exception handling part 1
"""try:
    list = [20, 0, 30]
    result = list[0] / list[1]
    print(result)
    print("Done")
except TypeError :
    print("Dividing by zero is not possible")
finally:
    print("Successfull")"""






# exception handling part 2
"""try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    result = num1 / num2
    print("result is ", result)
except (ValueError, ZeroDivisionError, SyntaxError, TypeError) :
    print("You have entered incorrect input . ")

finally:
    print("Thanks !!!")"""







# raise error handling
x = int(input("Enter your age : "))
def voter (x) :
    if x < 18 :
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"

try:
    print(voter(x))
except ValueError as e :
    print(e)












