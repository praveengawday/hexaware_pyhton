class P:
    def __init__(self,firstname,lastname):
        self.firstname=firstname;
        self.lastname=lastname;

    def display(self):
        print("my first name is :",self.firstname,"last name is :",self.lastname);


class C(P):
    def __init__(self,firstname,lastname):
        P. __init__(self,firstname,lastname)

c =C("praveen","kumar");
c.display();



