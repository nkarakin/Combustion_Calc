import math
import numpy as np 
'''
How many digits you have to move in order to get to the notation "0.X..."
Examples:
10.0    ->  2
1.0     ->  1
0.1     ->  0
0.01    ->  -1
0.001   ->  -2
0       ->  'inpiszero' 
'''
def get_dig_num(number):
    if abs(number) != 0:
        n = math.floor(math.log10(abs(number))+1)
    elif number == 0:
        n = 'inpiszero'
    return n

'''
The function returns a string representation of a number within given float definition:
If the number is not "visible" within defined float representation
the function switches to scintific notation.
'''

def formater(number, dig_t, dig_r):
    if dig_t < 7 or dig_r < 1 or dig_t - dig_r < 2:
        raise ValueError('This float representation is not allowed')
    
    if number > 0:
        if 10**(dig_t - dig_r - 1) <= round(number,dig_r): # Block 5

            return 'block 5'
        
        elif 10**(-dig_r) <= round(number, dig_r) < 10**(dig_t - dig_r - 1): # Block 4
            return 'block 4'
        
        elif round(number, dig_r) < 10**(-dig_r): # Block 3 p

            return f"{number/(10**get_dig_num(number)):0.02f}e+b3p"
    
    elif number < 0:
        
        if -10**(-dig_r) < round(number,dig_r): # Block 3 n
            a =  0
            exponent = get_dig_num(number)- a
            return f"{number/(10**exponent):.0{dig_t-6}f}e{exponent}" 
        
        elif -10**(dig_t - dig_r -2) < round(number,dig_r) <= -10**(-dig_r): # Block 2
            return '{num:{dt}.{dr}f}'.format(num=number, dt=dig_t,dr=dig_r)
        
        elif round(number, dig_r) <= -10**(dig_t - dig_r -2) : # Block 1
            a = 1 + (dig_t - 7) # 7 is the minimum allowed number for dig_t                  
            exponent = get_dig_num(number)- a
            return f"{number/(10**exponent):.01f}e+{exponent:02}" 
    
    elif number == 0:
        return 'number is zero'




a = [formater(x,10,2) for x in [-99.9*10**(9), -7777, -0.00000001, -0.001] ]
b = [get_dig_num(x) for x in  [-1000000, -0.000001, 0.001, -0.001] ]
print(a,b)
#import numpy as np 
#print(np.floor(4.6), int(4.6))
print('{num:{dt}.{dr}f}'.format(num=1444444444444, dt=3,dr=1))