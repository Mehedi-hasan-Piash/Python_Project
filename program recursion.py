
"""n = int(input("Enter any number for factorial result : "))
def fact (n) :
    if n == 1 :
        return 1
    else:
        return n * fact(n - 1)
print(fact(n))"""






n = int(input("Enter any number : "))

def fact (n) :
    if n == 1 :
        return 1
    else:
        return n * fact(n - 1)
result = fact(n)
print(result)









