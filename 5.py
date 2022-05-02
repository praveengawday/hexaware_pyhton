class Emp:
    '''def __init__(self,uid,name,age,salary,desig):
        self.uid=uid;
        self.name=name;
        self.age=age
        self.salary=salary;
        self.desig=desig;'''

    def __init__(self):
        self.uid=input("enter id :");
        self.name=input("enter name :");
        self.age=input("enter age:");
        self.salary=input("enter salary:")
        self.desig=input("enter desig:");


    def display(self):
        print("name :",self.name);
        print("id :",self.uid);
        print("age :",self.age);
        print("salary :",self.salary);
        print("desig:",self.desig);


#e=Emp(100,'praveen',22,400000,'clerk');    
e = Emp();
e.display();



