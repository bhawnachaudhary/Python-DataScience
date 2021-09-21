def add_3():
    x = input('X: ')
    y = input('Y: ')
    z = input('Z: ')
    TOTAL = int(x) + int(y) + int(z)
    return(TOTAL)

#using a valuereturning function    
add_3() #the answer will not be displayed and it will be lost

ans = add_3() #the answer will not be displayed but will be stored in answer variable
print(ans) #the variable can be used in code later


print(add_3())#the answer wi ll be displayed but not stored in any variable

output = add_3() + add_3() - add_3 #return type functions can be used 