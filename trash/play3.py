import math



print(int(math.log10(666222222.2)+1))

'''f-String displaying float numbers using scintific notation'''

'''
dig_lr: 
With this paramter you specify at what position a first none zero appears 
dig_lr > 0: The specified number of digits to the left from comma will be occupied
dig_lr = 0: The number will start with 0. 
dig_lr < 0: The specified number of digits to the RIGHT of the comma will be occupied with zeros

digits_r: 
This is a normal precision specifier for float numbers 

digits_exp: 
Defines how many digits you want in the exponent
'''

def fun(num,dig_lr,digits_r,digits_exp):
    if int(math.log10(abs(num))+1)-dig_lr >= 0: sign = '+'
    elif int(math.log10(abs(num))+1)-dig_lr < 0: sign = '-' 
    return f"{num/(10**(int(math.log10(abs(num))+1)-dig_lr)):.0{digits_r}f}e{sign}{abs(int(math.log10(abs(num))+1)-dig_lr):0{digits_exp}}"
    
print(fun(1,1,1,1))
# gives: 1.0e0

print(fun(1,0,1,1))
# gives: 0.1e1

print(fun(1,-3,3,1)) # Attension! -3 says that 3 digits after comma will be 0. And with precision = 3 you cant see the '1' any more! 
# gives: 0.000e4

print(fun(1,-3,4,1)) # Now you can see the '1'
# gives: 0.0001e4

print(fun(1,-3,4,3)) 
# gives: 0.0001e004

print(fun(-111,2,4,3)) 
# gives: 100.0000e-02
