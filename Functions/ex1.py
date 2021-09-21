def greet():
    print('Welcome to Wakanda')

def greetMore():
    print('*' * 20)
    print('Hi There')
    print('*'  * 20)

def greetPerson(name):
    greetMore()
    print(name,'You are not welcome here')
    #greet()

greet()
greetMore()
greetPerson('Bhawna')

greetPerson() #error