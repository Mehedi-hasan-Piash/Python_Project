"""import re
pattern = r"color"
if re.search(pattern, "Red is a color, I love red color"):
    print("Match")
else:
    print("Not Matched")"""






# search function
import re
pattern = r"color"
text = "My favourite color is Red"
match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())









