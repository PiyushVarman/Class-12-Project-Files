while True:
    sel=int(input('''1-Area of a Square
2-Volume of a cube
3-Total Surface Area of a Cuboid
4-Volume of a cone
5-Exit'''))
    if sel==1:      #Without argument and return
        def area():
            z=a**2
            print("Area is:",z)
        a=int(input("Enter the side:"))
        area()

    elif sel==2:    #With argument, without return
        def volumecube(a):
            z=a**3
            print("Volume is:",z)
        a=int(input("Enter the side:"))
        volumecube(a)

    elif sel==3:    #With return, without argument
        def TSA():
            z=2*(l*b+b*h+l*h)
            return(z)
        l,b,h=map(int,input("Enter the length, breadth and height:").split())
        print("The TSA is:",TSA())

    elif sel==4:
        def volumecone(r,h): #With return and argument
            z=(1/3)*3.14*(r**2)*h
            return(z)
        r,h=map(int,input("Enter the radius and the height:").split())
        print("The Volume of the Cone is:",volumecone(r,h))
        
    elif sel==5:
        break
