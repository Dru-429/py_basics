# List Comprehension Version
#nummber = [i for i in range(5)]

sq_nums = [i*i for i in range(5)]
print(sq_nums)

even_num = [i for i in range(10) if i%2 == 0]
print(even_num)

#matrix
matrix = [
  [1,2],
  [3,2]
]
print (matrix)
flat = []

for row in matrix:
  for num in row:
    flat.append(num)
print(flat)
#usinf list com.
#[expression for item in iterable]
flat = [num for row in matrix for num in row]

#lambda Function
# lambda input: output logic

square = lambda x: x*x
print(square(4))

students = [
    {"name": "Dru", "marks": 90},
    {"name": "Alex", "marks": 80}
]

students.sort(key = lambda student: student["marks"])
print(students)

#map: map(fn, set)
nums = [1,4, 2, 123, 21]
square = list(map(lambda x: x*x, nums))
print(square)

even = list(filter(lambda x: x%2==0, nums))
print(even)
