class Student:
    def __init__(self,name,age,salary):
        self.age=age;
        self._name=name;
        self.__salary=salary;

    def display(self):
        print("age :",self.age);
        print("name :",self._name);
        print("salary:",self.__salary);

s=Student("praveen",22,50000);
s.display();


