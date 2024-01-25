
# map function......
"""def square (x) :
    return x * x

num = [10, 20, 30, 40, 50]

result = list (map(square, num))
print(result)"""



# filter function........

"""num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

result = list (filter(lambda x : x%2==0, num))
print(result)"""









num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add (x) :
    return x%2==0

result = list(filter(add, num))
print(result)






