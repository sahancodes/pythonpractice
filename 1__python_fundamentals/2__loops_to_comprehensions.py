#cubes of odd numbers
num = [1, 2, 3, 4, 5]
cubes = [x**3 for x in num if x%2 == 1]
print(cubes)

#students who scored above 75
scores = {'Alice':82, 'Bob':67, 'Carol':91}
passed = [name for name, score in scores.items() if score > 75]
print(passed)

#squares of even numbers
nums = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in nums if x%2==0]
print(squares)

#words longer than 3 characters
words = ['a', 'abc', 'sahan', 'ac', 'kashmi']
long_words = [lngword for lngword in words if len(lngword)>=3]
print(long_words)