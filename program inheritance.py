
# Phone class => Parent class, Super class, Base class
# Samsung class => Child class, Sub class, Derived class

class Phone :
    def call (self):
        print("You can call")
    def message (self) :
        print("You can message")

class Samsung(Phone) :
    def call (self) :
        print("You can call")
    def messagge (self) :
        print("You can message")
    def photo (self) :
        print("You can take photo")

"""p = Phone()
p.call()
p.message()
s = Samsung()
s.call()
s.messagge()
s.photo()"""

x = Samsung()
x.call()
x.messagge()
x.photo()