#int to roman
def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result=""
        listVal=[1000,500,100,50,10,5,1]
        for i_index,i in enumerate(str(num)):
            temp=[]
            longg=len(str(num))-i_index-1
            realNumber=int(i)*(10**longg)
            for j in listVal:
                if("9" in str(realNumber) or ("4" in str(realNumber))) :
                        rounded=ceil(10**(longg))
                        temp.append(rounded)
                        realNumber+=rounded


                while(realNumber>=j):
                    
                    temp.append(j)
                    realNumber-=j
                if(realNumber==0):
                    break
            print(temp)
            for j in (temp): 
                if(j==1):
                    result+="I"
                elif(j==5):
                    result+="V"
                elif(j==10):
                    result+="X"
                elif(j==50):
                    result+="L"
                elif(j==100):
                    result+="C"
                elif(j==500):
                    result+="D"
                elif(j==1000):
                    result+="M"
        print(result)
        return result
        