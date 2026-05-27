# with open("data.txt", "w") as file:
#   file.write("Hello world !")
#   print("Succesfully writen")
  
with open("data.txt", "r") as file: 
  for i in file: 
    print(i)
  
  data = file.readlines()
  print(data)
#['Hello world !\n', "Now let's try multiple lines at once \n", 'line 01 ']
