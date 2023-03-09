

while True:
  Temp_Int = input("Please enter the temperature of the room: ")
  temp_vari = input("Is your temp in f, c, or k? ")
  if temp_vari == "f":
    temp_c = (float(Temp_Int) - 32) * (5 / 9)
    print("The temperature is", temp_c, "C")
    temp_k = (float(Temp_Int) - 32) * 5/9 + 273.15 
    print("The temperature is", temp_k, "K")  
    break
    
  elif temp_vari == "c":
    temp_k = float(Temp_Int) + 273.15
    print("The temperature is", temp_k, "K")
    temp_f = (float(Temp_Int) * 9 / 5) + 32
    print("The temperature is", temp_f, "F")
    break
  elif temp_vari == "k":
    temp_c = float(Temp_Int) - 273.15
    print("The temperature is", temp_c, "C")
    temp_f = (float(Temp_Int) - 273.15) * (5/9) + 32
    print("The temperature is", temp_f, "F")
    break
  else:
    print("sorry we didn't get your temperture type write")
    

