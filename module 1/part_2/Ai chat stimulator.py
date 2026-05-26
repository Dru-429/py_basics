def ai_response(userMsg, num) :
  print("Processing...")
  return f"{num}AI: AI response to ur message {userMsg}"

for i in range(2):
  msg = input("You:")
  try:
    output = ai_response(msg, i)
    print(output)
  except:
    print("Servers are busy, try later")
    break
    
