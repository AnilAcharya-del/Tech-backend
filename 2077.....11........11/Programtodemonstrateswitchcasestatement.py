
def switch():
    r = int(input("Enter Radius : ")) 
    h = int(input("Enter Height : ")) 
 

    print("Press 1 for Surface Area\n press 2 for Literal Area \n press 3 for Volume ")
     
    option = int(input(" your option : "))
 
    def Sar():
        result = 2*3.17*r*(r+h)
        print(" Surface Area Of Cylinder = ",result)
 
    def Lar():
        result = 2 * 3.17 * r * h
        print("Literal Area Of Cylinder = ", result)
 
    def vol():
        result = 3.17*r*r*h
        print("Volume Of Cylinder = ", result)
 
    def default():
        print("Incorrect option")
 
    dict = {
        1 : Sar,
        2 : Lar,
        3 : vol,
 
    }
    dict.get(option,default)()
 
 
switch()
 
