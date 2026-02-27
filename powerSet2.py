#program to find number of bits needed 

def totalflips(number1,number2):

    #var to count flips
    flips = 0

    #get the last bit of both numbers
    while(number1>0 or number2>0):
        t1 = (number1 & 1)
        t2 =(number2 & 1)
        if(t1!= t2):
            flips +=1


        number1>>=1
        number2>>=1

    return flips
number1 = int(input('enter your number'))
number2 = int(input('enter your number'))

print('\nnumber of flips needed',totalflips(number1,number2))
    