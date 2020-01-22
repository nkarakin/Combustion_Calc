def catch_errors(flag1,param1,flag2,param2,len_param1):
    import numpy as np
    import math
#----------------------------------------------------------------------------------------                  
    for value in param1:
        a=param1.index(value)
        if param1[a] < 0:
            raise ValueError

    if type(param2) == int or type(param2) == float:
        if param2 < 0:
            raise ValueError
    elif type(param2) == list:
        for value in param2:
            a=param2.index(value)
            if param2[a] < 0:
                raise ValueError
    elif param2 != 'none':
        raise ValueError
    
    if flag1 == 'massfrac' and flag2 == 'massflow_total':                    
        if type(param1) != list:
            raise TypeError          
        elif math.isclose(np.sum(param1),1,abs_tol = 0.00001) == False or len(param1) != len_param1:
            raise ValueError               
        elif type(param2) != int and type(param2) != float:
            raise ValueError

    elif flag1 == 'massfrac' and flag2 == 'moleflow_total':
        if type(param1) != list:
            raise TypeError
        elif math.isclose(np.sum(param1),1,abs_tol = 0.00001) == False or len(param1) != len_param1:
            raise ValueError               
        elif type(param2) != int and type(param2) != float:
            raise ValueError

    elif flag1 == 'massfrac' and flag2 == 'none':
        if type(param1) != list:
            raise TypeError
        elif math.isclose(np.sum(param1),1,abs_tol = 0.00001) == False or len(param1) != len_param1:
            raise ValueError
        elif param2 != 'none':
            raise ValueError
#-----------------------------------------------------------------------------------------
    elif flag1 == 'molefrac' and flag2 == 'massflow_total':                    
        if type(param1) != list:
            raise TypeError
        elif math.isclose(np.sum(param1),1,abs_tol = 0.00001) == False or len(param1) != len_param1:
            raise ValueError               
        elif type(param2) != int and type(param2) != float:
            raise ValueError

    elif flag1== 'molefrac' and flag2 == 'moleflow_total':
        if type(param1) != list:
            raise TypeError
        elif math.isclose(np.sum(param1),1,abs_tol = 0.00001) == False or len(param1) != len_param1:
            raise ValueError               
        elif type(param2) != int and type(param2) != float:
            raise ValueError

    elif flag1 == 'molefrac' and flag2 == 'none':
        if type(param1) != list:
            raise TypeError
        elif math.isclose(np.sum(param1),1,abs_tol = 0.00001) == False or len(param1) != len_param1:
            raise ValueError
        elif param2 != 'none':
            raise ValueError
#----------------------------------------------------------------------------------------
    elif flag1 == 'massflow_comp' and flag2 == 'none':
        if type(param1) != list:
            raise TypeError
        elif len(param1) != len_param1:
            raise ValueError
        elif param2 != 'none':
            raise ValueError
            
    elif flag1 == 'moleflow_comp' and flag2 == 'none':
        if type(param1) != list:
            raise TypeError
        elif len(param1) != len_param1:
            raise ValueError
        elif param2 != 'none':
            raise ValueError
    else:
        raise ValueError
        

