#Build a 2D matrix by taking input from user
#matrix = [[4,5,6],[7,8,9],[3,4,5]]

# 1,2,3
# 4,5,6
# 7,8,9

ROW=int(input("Enter the number of rows: "))
COLUMN=int(input("Enter the number of columns: "))

matrix=[]

#TODO: take input in a matrix
print("Enter the values in row: ")
for i in range(ROW):
    a=[]
    for j in range(COLUMN):
        a.append(int(input()))
    matrix.append(a)

#TODO: print the matrix
for i in range(ROW):
    for j in range(COLUMN):
        print(matrix[i][j],end=" ")
    print()
