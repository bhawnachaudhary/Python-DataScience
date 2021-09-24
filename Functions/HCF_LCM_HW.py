def hcf(num1,num2):
    if(num1>num2):
        small = num2
    else:
        small = num1
    for i in range(1,small):        
        if (num1%i == 0) and (num2%i ==0):                
            gcd = i
        else:
            continue                
    return gcd

print(hcf(54,24))



def compute_lcm(x, y):  
    # selecting the greater number  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm   

print(compute_lcm(8,12))