epafes={"Nikos":111222, "Maria": 333444}
#eisagwgh neas epafhs
print("Oi epafes einai: \n", epafes)
print("Dwse mia nea epafh: ")
name = input("Dwse onoma: ")
tel = input("Dwse arithmo thlefwnou: ")
epafes[name] = int(tel)
print("Oi epafes einai: \n", epafes)

#taksinomisi epafwn
epafes_list= list(epafes.items())
epafes_list.sort()
print("H taksinomimeni lista epafwn einai:\n", epafes_list)
