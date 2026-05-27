# List: Ordered, Mutable(change), allow dupliocates

nums = [1, 10, 4, 14, 5]
tools = ["chatgpt", "gemeni", "claude"]

for i in nums: 
  print(i)

print(tools[0])

tools.append("Perplexity")
print(tools)

tools[3] = "Cursor"
print(tools)

tools.insert(0, "OpenAI")
print(len(tools))
print(tools)

tools.remove("Cursor")

sort_Num = nums.sort()
print(nums)
print(sort_Num) #none

# append remove pop sort reverse clear 

#Tuples: List but immutable (unchangeable)
rgb = (255, 0, 0)
print(rgb[0])

# rgb[0] = 0 #error

#Sets: Unordered, Mutable, No duplicates
numbers = {1,20,4,1,1,5}
print(numbers) # {1, 20, 4, 5}

numbers.add(100)
nums.remove(1)

a = {1, 3, 5}
b = {0, 2, 4, 5} 

print(a.union(b))# {0, 1, 2, 3, 4, 5}
print(a | b)

print(a & b) # intersection

print(a - b) # difference: {1, 3}
print(b - a) # difference: {0, 2, 4}

# --- Dictionaries: Unordered, Mutable, No duplicates (keys), keys and values pairs
user = {
  "name": "John",
  "age": 30,
  "is_student": True
}

resopnse = {
  "statue" : 200, 
  "success": True,
  "data": {
    "id": 1,
    "name": "John"
  },
}

print(resopnse)
print(resopnse["data"])  #print(user["salary"])
#so use this 
print(resopnse.get("data")) #return none if not exits
print(resopnse["data"]["name"]) # John

resopnse["date"] = "2005-07-01"
print(resopnse)

user["age"] = 21
user["city"] = "New delhi"
print(user)
del user["city"]
print(user)

for key in user: 
  print(key, " : ", user[key])
  
for key, value in user.items():
    print(key, value)
    
#Methods: keys(), values(), items(), get(), pop(), clear()

users = [
    {
        "name": "Dru",
        "skills": ["Python", "React"]
    },
    {
        "name": "Alex",
        "skills": ["AI", "ML"]
    }
]

#list as a input

numbers = input("Enter numbers: ").split()
print(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)

numbers = set(map(int, input("Enter set values: ").split()))
#using set it will auto remove duplicates
print(numbers)

student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))

print(student)

data = {}
n = int(input("Enter the no of elements in dict: "))

for i in range(n) :
  key = input("Enter Key: ")
  val = input(f"Enter value for {key}: ")
  data[key] = val

print(data)                  

# List
# lst = list(map(int, input().split()))

# Tuple
# tpl = tuple(map(int, input().split()))

# Set
# st = set(map(int, input().split()))

# String List
# words = input().split()

# Float List
# floats = list(map(float, input().split()))                                                  