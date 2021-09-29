

z3=0
z4=0
z5=0
max=0
min=999
count = 0


age = int(input("Age "))

tbpm = 220-age


while True:
    bpm = int(input("number "))

    if bpm== 0:
        break

    if bpm > tbpm *0.7:
        z3 +=1
    elif bpm > tbpm *0.8:
        z4 +=1
    elif bpm > tbpm *0.9:
        z5 +=1  
    if bpm > max:
        max = bpm
    if bpm < min:
        min = bpm  

    count += 1

print("Results:")         
print("Zona 3 >(", tbpm*0.7,") :", round(z3/count/100))
print("Zona 4 >(", tbpm*0.8,") :", round(z4/count/100)) 
print("Zona 5 >(", tbpm*0.9,") :", round(z5/count/100))  
print("Max value : ", max) 
print("Min value : ", min)          

