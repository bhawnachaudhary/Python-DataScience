def armstrong():
    num = input('Enter a number')
    if num.isnumeric():
        power = len(num)   #stores no. of digits
        num = int(num)     #converts num into integer
        total = 0
        temp = num
        while temp > 0:
            r = temp % 10
            total += r ** power
            temp //= 10
        if num == total:
            print('Armstrong')
        else:
            print('Not Armstrong!')
    else:
        print('invalid input')


armstrong()
