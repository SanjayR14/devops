
array=[]
r=int(input("enter the row value:"))
c=int(input("enter the column value:"))
for i in range(r):
    row=[]
    for j in range(c):
        value=int(input(f"enter the value:({i},{j})"))
        row.append(value)
    array.append(row)
    
    print("answer")
print(array)

        
