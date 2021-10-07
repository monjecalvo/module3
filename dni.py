list = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:
    dni = input("Your DNI:")
    letter = dni[-1].upper
    number= dni[:-1]
    if(len(dni) == 9 and number.isdigit()):
        number= int(dni[:-1])
        break
    else:
        print("Format Incorrect")
r1=number%23
print(list[r1])
if list[r1] == letter:
    print("Correct")
else:
    print("Incorrect")    
