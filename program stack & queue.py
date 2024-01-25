
# proram stack start

"""books = []
books.append("Learn Python")
books.append("Learn C")
books.append("Learn C++")
books.append("Learn C#")
books.append("Learn Java")

books.pop()
books.pop()
print(books)
print("Now the top book is : ", books[-1])

books.pop()
print("Now the top book is : ", books[-1])

books.pop()
print("Now the top book is : ", books[-1])

books.pop()
if not books :
    print("No Books Left")"""

# program stack learn end




# program queue learn start


from collections import deque

bank = deque(["Tazmal", "Rifat", "Piash"])
bank.popleft()
bank.popleft()
bank.popleft()
print(bank)

if not bank :
    print("No person left")

# program queue learn end













