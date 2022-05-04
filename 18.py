import os.path

myfile =input("enter the file to want to write?");
mf=os.path.exists(myfile);

if mf:
    f=open(myfile,"w");
    name=input("enter the name :");
    age=input("enter the age :");
    salary=input("enter the salary:");
    desig=input("enter the desig:");
    myrecord=[name, age, salary, desig ]

    for i in myrecord :
         f.write(i);
         f.write('\t');


    f.close();

else:
    print("sorry file doesnt existance...");

    
print("======read==");
myfileread =input("enter the file to want to read from?");
fr=open(myfileread,"r");

for i in fr:
     print(i);
     
