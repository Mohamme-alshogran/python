class Item :
    name = " "
    price = 0.0
    def __init__(self,name ,price):
        self.name = name
        self.price = price
    def printItem (self) :
        print(self.name + " ->"+str(self.price))
    def discount (self,discount):
        self.price = self.price - self.price * discount
class Mune :
    def __init__(self):
        self.items = [
            Item("minsaf",20),
            Item("shawram", 15.5),
            Item("pizza", 10),
            Item("kabsa", 7.5),

        ]
    def printMune (self) :
        for item in self.items :
            item.printItem()
    def discountMune (self ,discount) :
        if 0.05 <= discount <= 0.4:
            for item in self.items :
                item.discount(discount)

                item.printItem()
        else:
            print("worng discount ")
print(" welcom to our restrant")
while (True) :
    print( " please input yor chioce")
    print("1-print mune")
    print("2-input discount ")
    mune = Mune()
    try:
        choice = int(input())

        if choice == 1:
            mune.printMenu()
        elif choice == 2:
            print("input discount between 0.05 and 0.4")
            discount = float(input())
            mune.discountMune(discount)
        else:
            print("wrong input")
    except ValueError:
        print("wrong input")

