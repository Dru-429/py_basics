#conditions 
user_prompt = input("Enter prompt: ")

if len(user_prompt) > 200:
  print("Prompt too long")
elif len(user_prompt) <2: 
  print("Prompt is tooo small")
else:
  print("Sending to AI model...")
  
#loops
for i in range(5):
  print(i)
#  range(start, stop, step)
#  Step isn't included in the range

for i in range(10):
  if i == 1:
    pass
  if i == 2:
    continue
  if i == 4:
    break
  print(i)

tools = ["ChatGPT", "Claude", "Gemini"]

for tool in tools:
  print(tool)
  

#functions
def greet(name="User"):
  print(f"Hello {name}")
  
def student(name, age):
    print(name, age)

student(age=20, name="Dru")
def student(name, age):
  print(name, age)

student(age=20, name="Dru")  

#global
count = 0

def increase():
  global count
  count += 1
  print(count)

increase()

#try-catch
try:
  num = int(input("Enter a num: "))
  print(num)
except: 
  print("invalid Input")

try:
  number = int(input("enter num: "))
except ValueError:
  print("Invalid number")
except Exception as e:
  print(e)
finally: 
  print("Finally blocks always run wether its error or run")
  
  