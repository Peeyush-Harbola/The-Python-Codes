#taking user defined input
A = list(map(int,input("Enter your List here:").strip().split(" ")))

A.sort() #sorting the list

print("Sorted List:",A)

count=0
maxcount=0       #current element
t=0
for i in A:
    if i==maxcount:
        count+=1
        if count==(len(A)//2):
            print(maxcount)
            t=1
        
    else:
        
        count=1
        maxcount=i

if t==0:
    print("No such Element found")
