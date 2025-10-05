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

# convert temperatures from celcius to farenheit
# farenheit = (celcius * 1.8) + 32
celcius = [0, 10, 20, 30, 40]
farenheit = []
for temp in celcius:
    farenheit.append(temp * 1.8 + 32)
print(farenheit)
# short form -> first calculation -> for loop
farenheit_2 = [temp_2 * 1.8 + 32 for temp_2 in celcius]
print(farenheit_2)

# Filter names starts with a vowel
names = ['Alice', 'Bob', 'Eve', 'Uma', 'Oscar']
nameswithvowels = []
for name in names:
    if name.startswith(('A','E','I','O',"U")):
       nameswithvowels.append(name)
print(nameswithvowels) 
# short form
nameswithvowels_2 = [name for name in names if name.startswith(('A','E','I','O',"U"))]
print(nameswithvowels_2)

#Create a dictionary of numbers and their cubes (1–5)
nums_c = [1,2,3,4,5]
cub_nums = {}
for num_c in nums_c:
    cub_nums.__setitem__(num_c,num_c**3)
print(cub_nums)
# short form
cub_nums_2 = {n: n**3 for n in nums_c}
print(cub_nums_2)

