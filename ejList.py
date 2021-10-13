theList = []
while True:
    print("1.- Add a number to the list ")
    print("2.- Add a number in a position in the list ")
    print("3.- Show the length of the list ")
    print("4.- Delete the last number in the list ")
    print("5.- Delete a number in the list ")
    print("6.- Count numbers ")
    print("7.- Positions of a numbers ")
    print("8.- Show the list ")
    print("9.- Exit ")
    option = int(input("Chosse an option:"))
    if option == 1:
        num = int(input("Input a number"))
        theList.append(num)
    elif option == 2:
        num = int(input("Input a number"))
        pos = int(input("Input the position"))
        if pos <= len(theList):
            theList.insert(pos,num)
        else:
            print("out of position")    
    elif option == 3:
        print(len(theList))
    elif option == 4:
        if len(theList) > 0:
            print("The last elmenent is",theList.pop)
    elif option == 5:
        pos = int(input("Input the position"))
        if pos <= len(theList):
            theList.pop(pos)
    elif option == 6:
        num = int(input("Input the number"))
        print(num, theList.count(1))
    elif option == 7:
        num = int(input("Input the number"))
        pos = 0
        for elem in range(0,theList.count(num)):
            index = theList.index(num,pos)
            print(index, end=" ")
            pos = index + 1
        print()
        """index = 1
        for elem in theList:
            if elem == num:
                print(index, end=" ")
            index += 1
        print()"""    
    elif option == 8:
        for elem in theList:
            print(elem,end=" ")
        print()    
    elif option == 9:
        break    