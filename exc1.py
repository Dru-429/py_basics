# Mini project: 

name= input('enter ur name: ')
role = input('enter ur role:')
goal = input("What u wan to learn? ")

prompt = f"""
You are a AI mentor. 

student namee: {name}
role: {role}
goal: {goal}

Generate a personalized learning path for the student to achieve their goal.
"""

print(prompt)