arr=input("List of number :").split(' ')
streak=0
def answ():
    for i in arr: 
        if(i%2==0):
            streak=0
           
        elif(i%2==1):
            streak+=1
            if(streak==3):
               return True 
    return False