class Demo:
    def __init__(self):
        try:
            a=int(input("enter the value of A"));
            b=int(input("enter the value of B"));
            c=a/b;
            print("res:  ",c);

        except :
             print("cant diivide by 0");
        finally:
             print("thank you");
        
d=Demo();
