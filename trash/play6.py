import math
def fun(number,digits_total, digits_r_min, digits_r_max, digits_r_start):
    if  10**(-digits_r_start) <=  round(number,digits_r_start) < 10**(digits_total-digits_r_start-1):
        return f"{10**(-digits_r_start):>10} <=" + '{num:{dt}.{dr}f}'.format(num=number, dt=digits_total,dr=digits_r_start) + f" < {10**(digits_total-digits_r_start-1):<}"
    
    for x in range(digits_r_start,digits_r_min,-1):
        
        if 10**(digits_total-x-1) <=  round(number,x-1) < 10**(digits_total-x):
            return f"{10**(digits_total-x-1):>10} <=" + '{num:{dt}.{dr}f}'.format(num=number, dt=digits_total,dr=x-1) + f" < {10**(digits_total-x):<}"
       
    if 10**(digits_total-digits_r_min-1) <= round(number,digits_r_min)  :
        #print('hi')
        dig_lr = digits_total - digits_r_start - 1
        digits_r = digits_r_start - 3 # 3 for scintifec notation
        digits_exp = 1 # 3 digits will be occupied. example: e+4
        if int(math.log10(number)+1)-dig_lr >= 0: sign = '+'
        elif int(math.log10(number)+1)-dig_lr < 0: sign = '-' 
        return f"{number/(10**(int(math.log10(number)+1)-dig_lr)):.0{digits_r}f}e{sign}{abs(int(math.log10(number)+1)-dig_lr):0{digits_exp}}"
    
        



  
digits_total = 9
digits_r_min = 1
digits_r_max = 48888
digits_r_start = 5
        


print(fun(0.0001, digits_total,digits_r_min,digits_r_max,digits_r_start))
print(fun(99.999996,digits_total,digits_r_min,digits_r_max,digits_r_start))
print(fun(9999.99996,digits_total,digits_r_min,digits_r_max,digits_r_start))
print(fun(99999.9996,digits_total,digits_r_min,digits_r_max,digits_r_start))
print(fun(999999.996,digits_total,digits_r_min,digits_r_max,digits_r_start))
print(fun(9999999.96,digits_total,digits_r_min,digits_r_max,digits_r_start))
