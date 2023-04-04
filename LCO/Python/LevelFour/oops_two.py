#Inheritance
#parent class
class Samsung:
    def __init__(self):
        print("I am Samsung")
    def makeScreen(self):
        print("I make screen: Samsung")
    def test(self):
        print("Screen Test 1: OK")
        print("Screen Test 2: OK")
        print("Screen Test 3: OK")

#child class
class Iphone(Samsung):
    def __init__(self):
        print("I am Iphone")
        super(Iphone, self).__init__()
    def a3Chips(self):
        print("I make a3 bionic chips")
    def itest(self):
        print("a3 CHIP Test: OK")
        super().test()
    def makeScreen(self):
        print("I make screen: Apple")



user=Iphone()
user.a3Chips()
user.makeScreen()
user.itest()