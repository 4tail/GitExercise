class Work:
    def __init__(self , volt) :
        self.volt = volt
    
    #1023
    def ToDigital(self):
        num = self.volt/5
        numberofdigit = num*1023
        return(bin(int(numberofdigit))[2:])
    
    def SetDigiotalValue(value,self):
        str(print(value))
    
    def printvolt(self):
        print(self.volt)



t1 = Work(4)

t1.printvolt()
print(t1.ToDigital())

t1.SetDigiotalValue(1100110010)     

t1.printvolt()