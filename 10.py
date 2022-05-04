class Cal:
    def addation(self,a,b):
        print(a+b);

class MyCal:
    def sub(self,a,b):
        print(b-a);

class Cal2( Cal ,MyCal):
    def multi(self,a,b):
        print(a*b);

c2=Cal2();
c2.addation(100,600);
c2.multi(10,20);
c2.sub(200,100);
