# required Parameter
def adder(a,b,c):
    return a+b+c

# adder(1,3,2)
# adder(3,3,3)
# adder(1,3) #error







# Default parameter
def multiplier(a,b,c=2):
    return a*b*c

# multiplier(2,2) # c will take default value as 2
# multiplier(2,2,3) # c will take 3







def divisor(a,b=1,c=1):
    return a/b/c



if __name__ == "__main__":  #this condition will run below function calls only in this page but for other pages these will not be run
    divisor(1)
    divisor(1,2)
    divisor(2,1,2) #or# 
    divisor(a=2,b=1,c=1) #named argument    #or#
    divisor(2,b=1,c=1)  #etc..
    divisor()   # error



# print('hola',end = '--')












def pythageorous(perpendicular=1,base=1):
    hyp = (perpendicular ** 2 + base ** 2) ** 0.5
    return hyp

# pythageorous()