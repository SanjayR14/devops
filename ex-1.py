r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

array = [[int(input(f"Enter value ({i},{j}): ")) for j in range(c)] for i in range(r)]

print("\nAnswer:")
for row in array:
    print(row)
