print("Hello world!")

# Variables and Data types
x = 5
print(type(x))
name = "Dru"
print(type(name))
age = 20
height = 5.9
is_dev = True

print(name)
print(type(name))
print(age)
print(height)
print(is_dev)
print( x + age)
print( x + name)

# Operators
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # module op. sends remender 

# input and output
name = input("Enter Name: ")
city = input("Enter city: ")
age = int(input("Enter age: "))
print(type(age))

#print methode 1 
print(f"I am {name} and I live in {city}, aged {age} years old")

#print methode 3
print("I am {} and I live in {}, aged {} years.".format(name, city, age))

#string
text = "Python3"
text2 = "Artificial Intelligence"


print(text[0])
print(text[-7])
print(text[-1])
print(type(text[-1])) # class str

msg = "learning ai using chatgpt"

print(msg.upper())
print(msg.title())
print(msg.replace("chatgpt", "python"))
print(msg[0])

# print("Hello " + 5)
print(f"Hello {5}" )
