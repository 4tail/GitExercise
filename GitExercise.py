class Work:
    def __init__(self , volt) :
        self.volt = volt
    
    #1023
    def ToDigital(self):
        num = self.volt/5
        numberofdigit = num*1023
        return(bin(int(numberofdigit))[2:])
    
    def SetDigiotalValue(self,value):
        
        num = int(str(value),2)
        self.volt = (num/1023)*5



    
    def printvolt(self):
        print(self.volt)



t1 = Work(2)

print(t1.ToDigital())
num = 1100110010
t1.SetDigiotalValue(int(num))     
