import math
def fun(number,digits_total, digits_r):
    if  10**(-digits_r) <=  round(number,digits_r) < 10**(digits_total-digits_r-1):
        print (f"{10**(-digits_r):>10} <=" + '{num:{dt}.{dr}f}'.format(num=number, dt=digits_total,dr=digits_r) + f" < {10**(digits_total-digits_r-1):<}")
        return                               '{num:{dt}.{dr}f}'.format(num=number, dt=digits_total,dr=digits_r)
    elif -10**(digits_total-digits_r-1-1) < round(number,digits_r) <= -10**(-digits_r):    
        print( '{num:{dt}.{dr}f}'.format(num=number, dt=digits_total,dr=digits_r))
        return '{num:{dt}.{dr}f}'.format(num=number, dt=digits_total,dr=digits_r) 
    elif -10**(-digits_r) < round(number, digits_r) < 10**(-digits_r):
        dig_lr = 0
        digits_r = 4
        digits_exp = 1
        if int(math.log10(abs(number))+1)-dig_lr >= 0: sign = '+'
        elif int(math.log10(abs(number))+1)-dig_lr < 0: sign = '-' 
        print (f"{number/(10**(int(math.log10(abs(number))+1)-dig_lr)):.0{digits_r}f}e{sign}{abs(int(math.log10(abs(number))+1)-dig_lr):0{digits_exp}}")



def fun2(number):
    if abs(number) != 0:
        n = int(math.log10(abs(number))+1)
    elif number == 0:
        n = 'inpiszero'
    return n

print(fun2(10))
print(fun2(1))
print(fun2(0.1))
print(fun2(0.01))
print(fun2(0))

