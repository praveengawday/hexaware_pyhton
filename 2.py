
def abc():
 for i in range(10):
    print("function:",i)

abc();

class demo:
    def __init__(self):
        for i in range(10):
            print("constructor :",i);


    def display(self):
        for i in range(10):
            print("method :",i);

d=demo();
d.display()
