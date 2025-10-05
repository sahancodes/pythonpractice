#zip always result in a set of tuples
a = [1,2,3]
b = ['a','b','c']

zipped = list(zip(a,b))
print(zipped) #[(1, 'a'), (2, 'b')]

#Transpose using zip
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# *matrix means - remove the outer list in the matrix list (it becomes a three lists)
# *matrix => [1,2,3],[4,5,6],[7,8,9]
# zip(*matrix) => (1,4,7),(2,5,8),(3,6,9) - results in a set of tuples
# map(list, zip(*matrix)) - converts the tuples above into lists => [1,4,7],[2,5,8],[3,6,9]
# list(map(list, zip(*matrix))) adds a list on top of the three lists to make it a matrix
transposed = list(map(list, zip(*matrix)))
print(transposed)

# this yields the same result
transposed_x = list(list(col) for col in zip(*matrix))
print(transposed_x)


# Pair names with scores
names  = ["Ada", "Grace", "Linus", "Guido"]
scores = [98, 87, 91, 95]
paired = [f"{pair[0]}: {pair[1]}" for pair in zip(names,scores)]
print(paired)
# -> ["Ada: 98", "Grace: 87", ...]

# Unzip back into two lists (star-unpack)
pairs = [("A", 1), ("B", 2), ("C", 3)]
pairs_lst = list(map(list, zip(*pairs)))
print(f"Letters:  {pairs_lst[0]}, Nums: {pairs_lst[1]}")
# -> letters = ["A","B","C"], nums = [1,2,3]


# Ragged transpose (zip_longest)
from itertools import zip_longest

ragged = [[1,2,3],[4,5],[6,7,8,9]]
rag_tps = list(map(list, zip_longest(*ragged, fillvalue=None)))
print(rag_tps)