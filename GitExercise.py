class Work:
    def __init__(self , volt,maxvolt,numofbits) :
        self.volt = volt
        self.maxvolt = maxvolt
        self.numofbits = numofbits
        
    #((2**self.numberofbits) - 1)
    #1023
    def ToDigital(self):
        num = self.volt/self.maxvolt
        numberofdigit = num*((2**self.numofbits) - 1)
        return(bin(int(numberofdigit))[2:])
    
    def SetDigiotalValue(self,value):
        
        num = int(str(value),2)
        self.volt = (num/((2**self.numofbits) - 1))*self.maxvolt



    
    def printvolt(self):
        print(self.volt)
    




t1 = Work(15,20,8)
print(t1.ToDigital())
t1.SetDigiotalValue(10011001)
t1.printvolt()