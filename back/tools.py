import numpy as np
import random 

def formater(number, dig_t, dig_r):
    if dig_t < 7 or dig_r < 1 or dig_t - dig_r < 2:
        raise ValueError('This float representation is not allowed')
    
    if number > 0:

        if 10**(dig_t - dig_r - 1) <= round(number,dig_r): 
            a = np.float32(number)
            return np.format_float_scientific(a, unique=False, exp_digits=2, precision=dig_t-6)
        
        elif 10**(-dig_r) <= round(number, dig_r) < 10**(dig_t - dig_r - 1): 
            s = '{num:{dt}.{dr}f}'.format(num=number, dt=dig_t,dr=dig_r)
            return s
        
        elif round(number, dig_r) < 10**(-dig_r): 
            a = np.float32(number)
            return np.format_float_scientific(a, unique=False, exp_digits=2, precision=dig_t-6)
    
    elif number < 0:
        
        if -10**(-dig_r) < round(number,dig_r): 
            a = np.float32(number)
            return np.format_float_scientific(a, unique=False, exp_digits=2, precision=dig_t-6-1)
        
        elif -10**(dig_t - dig_r -2) < round(number,dig_r) <= -10**(-dig_r): 
            return '{num:{dt}.{dr}f}'.format(num=number, dt=dig_t,dr=dig_r)
        
        elif round(number, dig_r) <= -10**(dig_t - dig_r -2) : 
            a = np.float32(number)
            return np.format_float_scientific(a, unique=False, exp_digits=2, precision=dig_t-6-1)
    
    elif number == 0:
        return  '{num:{dt}.{dr}f}'.format(num=number, dt=dig_t,dr=dig_r)

def rand_gen(minimum, maximum):
    choice = ['int','float']
    pick = random.choice(choice)
    if pick == 'int':
        return random.randint(int(minimum),int(maximum))
    elif pick == 'float':
        return random.uniform(minimum,maximum)

def rand_gen_vec(length,minimum,maximum):
    return [rand_gen(minimum,maximum) for x in range(0,length)]
