
# non lambda...
"""def calculate (a, b) :
    return a*a + 2*a*b + b*b
print(calculate(2, 3))"""



# lambda function ........

x = (lambda a, b : a*a + 2*a*b + b*b) (2, 3)
print(x)



a = (lambda x : x*x*x)(5)
print(a)