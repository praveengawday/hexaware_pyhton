class Clerk :
    salary=15000;
    desig="CLERK";


    def __init__(self):
        self.uid=input("enter id :");
        self.name=input("enter name :");
        self.age=input("enter age:");
       


    def display(self):
        print("name :",self.name);
        print("id :",self.uid);
        print("age :",self.age);
        print("salary :",self.salary);
        print("desig:",self.desig);

    def raiseSal(self):
        print("name :",self.name);
        print("id :",self.uid);
        print("age :",self.age);
        print("salary :",self.salary+20000);
        print("desig:",self.desig);


#e=Emp(100,'praveen',22,400000,'clerk');    
e = Clerk();
e.display();
e.raiseSal();
