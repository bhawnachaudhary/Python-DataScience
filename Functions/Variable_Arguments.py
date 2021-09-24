# variable number of arguments can be passed
def avg(*numbers):
    if numbers:
        return sum(numbers)/len(numbers)



def guestList(*guestname):
    print("these are the guests for the event!!")
    for name in guestname:
        print('!!!',name,'!!!')
    
if __name__ == "__main__":
    a = avg(12,3,54,8,33,2,1,7,9)
    b = avg()#error because no arguments passsed
    c = avg(12,13,11)
    print(a)
    guestList('raju','shaka','rohan','dev','devi')

