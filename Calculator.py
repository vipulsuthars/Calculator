class calci:
    
    def string(self,c1,c2):
        c1 = c1.split('.')
        c2 = c2.split('.')
        print(c1)
        print(c2)
        if len(c1)==1 and len(c2) == 1:
            return ( int(c1[0]) , int(c2[0]) )
        else:
            if len(c1) == 1 and len(c2)!=1:
                return float(c1[0]) , float(c2[0]+'.'+c2[1])
            else:
                return float(c1[0]+'.'+c1[1]) , float(c2[0])

    def add(self,a,b):
        a , b  = self.string(a,b)
        t = a+b
        t = str(t)
        t = t.split('.')
        if len(t) == 1:
            return int(t[0])
        return float(t[0]+'.'+t[1][:3])
        
    def sub(self,a,b):
        a , b  = self.string(a,b)
        t = a - b
        t = str(t)
        t = t.split('.')
        if len(t) == 1:
            return int(t[0])
        return float(t[0]+'.'+t[1][:3])
    
    def mul(self,a,b):
        a , b  = self.string(a,b)
        return a * b
 
    
    def div(self,a,b):
        if b==0:
            return "error"
        return a/b
    
    def percentage(self,a,b):
        per = input("How Much Percentage You Want ")
        print("Percentage is = ", (self.add(a,b) * float(per) )/100)

object = calci()
while(True):
    n1 = input("Enter your First Number : ")
    n2 = input("Enter your Second Number : ")

    Message = input("Enter What Do You Want to Do:\n 1 for Addition \n 2 for Subtraction\n 3 for Multiplication \n 4 for Division \n 5 for Percentage \n 6 for Exit \n")

    if int(Message) == 1:
        print("Addition is =  " , object.add(n1,n2))
    elif int(Message) == 2:
        print("Subtraction is =  ", object.sub(n1,n2))
    elif int(Message) == 3:
        print("Multiplication is =  ", object.mul(n1,n2))
    elif int(Message) == 4:
        print("Division is =  ", object.div(n1,n2))
    elif int(Message) == 5:
        object.percentage(n1,n2)
    else:
        print("Ended Succcessfully!!!!")