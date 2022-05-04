list=[10,20,30,40,50,60,60]
print(list);

data={10,20,30,40,50,60,60};
print(data);

data.add(100);
data.remove(20);
data.pop();

for i in data:
    print(i);
    

print("----------");
print("before sorting:",data);
mydata=sorted(data)
print("after sorting:",mydata);
