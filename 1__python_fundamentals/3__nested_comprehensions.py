# Flatten a 2D list
matrix1 = [[1, 2], [3, 4], [5, 6]]
lst = []
for i in matrix1:
    for j in i:
        lst.append(j)
# short form [new var (l) -> nested loop -- outer loop first (k in matrix)  -> inner loop (l in k)]

lst2 = [l for k in matrix1 for l in k]
print(lst, lst2)

# Extract even numbers only
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8]]
reslst2 = []
for row2 in matrix2:
    for element2 in row2:
        if element2 % 2 == 0:
            reslst2.append(element2)
#short form
reslst2_x = [element2x for row2 in matrix2 for element2x in row2 if element2x%2==0]
print(reslst2, reslst2_x)


# Transpose a matrix (swap rows and columns)
matrix3 = [[1, 2, 3], [4, 5, 6]]
reslst3 = []
for col3 in range(len(matrix3[0])):
    reslst3.append([])
    for row3 in matrix3:
        reslst3[col3].append(row3[col3])
# short form
reslst3_x = [[row3x[col3x] for row3x in matrix3] for col3x in range(len(matrix3[0])) ] 

# short form 2
# zip(*matrix) unpacks the rows and zips them column-wise (the transpose) "tuples"
# list() converts the tuples into lists
transpose = [list(col3) for col3 in zip(*matrix3)]

print(reslst3, reslst3_x, transpose)

# Generate coordinate pairs (i, j) for a grid
rows, cols = 2, 3
cordinates = []
for i4 in list(['a','b']):
    for j4  in list([1,2,3]):
        cordinates.append([i4, j4])
# short form
cordinates_x = [[i4x, j4x] for i4x in list(['a', 'b']) for j4x in list([1,2,3])]
print(cordinates, cordinates_x)


# Flatten but only strings
mixed = [[1, "a", 2], ["b", 3, "c"], [4, "d"]]
flatstr = [ele5 for row5 in mixed for ele5 in row5 if isinstance(ele5, str)]
print(flatstr)


#Flatten only upper triangle of a matrix (i ≤ j)
matrix5 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
uptriangle = []
uptrianglexx = []
# uptrianglexx = []
# enumerate() function is used to get the position of a value in a matrix as (i,j)
# range() create a list of numbers to iterate in for loops  range(start, stop, step)
for p5,i5 in enumerate(matrix5):
    for k5 in range(3-p5):
        uptriangle.append(i5[k5])   
# The above is wrong because the triangle is the other side 
for i55 in range(len(matrix5)):
    for j55 in range(i55, len(matrix5)):
        uptrianglexx.append(matrix5[i55][j55])
uptrianglex = [matrix5[i55][j55] for i55 in range(len(matrix5)) for j55 in range(i55,len(matrix5))]
print(uptriangle, uptrianglex, uptrianglexx)


# Create a multiplication table (nested comprehension)
n = 3
prod_temp = []
product = []
productx = []
for i6 in range(1,n+1):
    prod_temp.clear()
    for j6 in range(1, n+1):
        print(i6, j6)
        prod_temp.append(j6*i6)
    product.append(list(prod_temp))
# short form
productx = [[i6x*j6x for j6x in range(1,n+1)] for i6x in range(1,n+1)]
print(product, productx)



# Cartesian product of two lists
A = [1, 2]
B = ['x', 'y', 'z']
cart_prod = [[f"{B[B.index(i7)]}{A[A.index(j7)]}" for i7 in B] for j7 in A]
print(cart_prod)