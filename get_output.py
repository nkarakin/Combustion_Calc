def get_output(fuel, air, flue, comb):
    
    import numpy as np
    SCIENTIFIC_NOTATION_WIDTH = 4
    def my_format(number, n):
        if number == 0:
            places = 0
        else:
            places = np.log10(np.abs(number))            
        
        highest_place = -int(places)
        if 1 <= highest_place < 3:
            rounded = np.round(number, n - highest_place - 1)
        elif highest_place >= 3:
            rounded = np.round(number, highest_place + n - 5)
        elif -n < highest_place < 1:
            rounded = np.round(number, n + highest_place - 2)
        else:
            rounded = np.round(number, highest_place + n - 6)
        return "{{:{}.{}g}}".format(n,n).format(rounded)
#--------------------------------------------------------------------------------------------------------    
    comp = ['CO2','H2O','N2','Ar','O2','SO2','CO','H2','CH4','H2S','C2H6','C3H8']
    elem = ['C','H','O','S','N','Ar']        
    num_C =  [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 3]
    num_H =  [0, 2, 0, 0, 0, 0, 0, 2, 4, 2, 6, 8]
    num_O =  [2, 1, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0]
    num_S =  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    num_N =  [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_Ar = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
#--------------------------------------------------------------------------------------------------------    
    fuel_massfrac = fuel.get_massfrac()
    fuel_molefrac = fuel.get_molefrac()
    fuel_massflow_comp = fuel.get_massflow_comp()
    fuel_moleflow_comp = fuel.get_moleflow_comp()
    fuel_massflow_total = fuel.get_massflow_total()
    fuel_moleflow_total = fuel.get_moleflow_total()
    fuel_sum_massfrac = np.sum(fuel_massfrac)
    fuel_sum_molefrac = np.sum(fuel_molefrac)
    
    fuel_maf_conv = []
    fuel_mof_conv = []
    fuel_mafl_conv = []
    fuel_mofl_conv = []

    for element in fuel_massfrac:    
        fuel_maf_conv.append(my_format(element,6))
    for element in fuel_molefrac:    
        fuel_mof_conv.append(my_format(element,6))
    for element in fuel_massflow_comp:    
        fuel_mafl_conv.append(my_format(element,6)) 
    for element in fuel_moleflow_comp:    
        fuel_mofl_conv.append(my_format(element,6))
    fuel_sum_massfrac = my_format(fuel_sum_massfrac,6)
    fuel_sum_molefrac = my_format(fuel_sum_molefrac,6)
    fuel_massflow_total = my_format(fuel_massflow_total,6)
    fuel_moleflow_total = my_format(fuel_moleflow_total,6)

    print('FUEL             |', end='')
    for value in comp:
        print("{0:>7}".format(value),end='')
    print("{0:>7}".format('SUM'))
    
    print('massfrac [-]     |', end = '')    
    for value in fuel_maf_conv:
         print("{0:>7}".format(value), end = '')
    print("{0:>7}".format(fuel_sum_massfrac))

    print('molefrac [-]     |', end = '')    
    for value in fuel_mof_conv:
        print("{0:>7}".format(value), end = '')
    print("{0:>7}".format(fuel_sum_molefrac))
    
    print('massflow [kg/s]  |', end = '')    
    for value in fuel_mafl_conv:
        print("{0:>7}".format(value), end = '')  
    print("{0:>7}".format(fuel_massflow_total))
    
    print('moleflow [mol/s] |', end = '')    
    for value in fuel_mofl_conv:
        print("{0:>7}".format(value), end = '')   
    print("{0:>7}".format(fuel_moleflow_total))  
    print('\n')
#--------------------------------------------------------------------------------------------------
    air_massfrac = air.get_massfrac()
    air_molefrac = air.get_molefrac()
    air_massflow_comp = air.get_massflow_comp()
    air_moleflow_comp = air.get_moleflow_comp()
    air_massflow_total = air.get_massflow_total()
    air_moleflow_total = air.get_moleflow_total()
    air_sum_massfrac = np.sum(air_massfrac)
    air_sum_molefrac = np.sum(air_molefrac)
    
    air_maf_conv = []
    air_mof_conv = []
    air_mafl_conv = []
    air_mofl_conv = []
    
    for element in air_massfrac:    
        air_maf_conv.append(my_format(element,6))
    for element in air_molefrac:    
        air_mof_conv.append(my_format(element,6))
    for element in air_massflow_comp:    
        air_mafl_conv.append(my_format(element,6))
    for element in air_moleflow_comp:    
        air_mofl_conv.append(my_format(element,6))
    air_sum_massfrac = my_format(air_sum_massfrac,6)
    air_sum_molefrac = my_format(air_sum_molefrac,6)
    air_massflow_total = my_format(air_massflow_total,6)
    air_moleflow_total = my_format(air_moleflow_total,6)
        
    print('AIR              |')    
    print('massfrac [-]     |', end = '')    
    for value in air_maf_conv:
         print("{0:>7}".format(value), end = '')
    print("{0:>7}".format(air_sum_massfrac))

    print('molefrac [-]     |', end = '')    
    for value in air_mof_conv:
        print("{0:>7}".format(value), end = '')
    print("{0:>7}".format(air_sum_molefrac))
    
    print('massflow [kg/s]  |', end = '')    
    for value in air_mafl_conv:
        print("{0:>7}".format(value), end = '')  
    print("{0:>7}".format(air_massflow_total))
    
    print('moleflow [mol/s] |', end = '')    
    for value in air_mofl_conv:
        print("{0:>7}".format(value), end = '')   
    print("{0:>7}".format(air_moleflow_total))  
    print('\n')
#-------------------------------------------------------------------------------------------------------
    flue_massfrac = flue.get_massfrac()
    flue_molefrac = flue.get_molefrac()
    flue_massflow_comp = flue.get_massflow_comp()
    flue_moleflow_comp = flue.get_moleflow_comp()
    flue_massflow_total = flue.get_massflow_total()
    flue_moleflow_total = flue.get_moleflow_total()
    flue_sum_massfrac = np.sum(flue_massfrac)
    flue_sum_molefrac = np.sum(flue_molefrac)
    
    flue_maf_conv = []
    flue_mof_conv = []
    flue_mafl_conv = []
    flue_mofl_conv = []
    
    for element in flue_massfrac:    
        flue_maf_conv.append(my_format(element,6))
    for element in flue_molefrac:    
        flue_mof_conv.append(my_format(element,6))
    for element in flue_massflow_comp:    
        flue_mafl_conv.append(my_format(element,6)) 
    for element in flue_moleflow_comp:    
        flue_mofl_conv.append(my_format(element,6))
    flue_sum_massfrac = my_format(flue_sum_massfrac,6)
    flue_sum_molefrac = my_format(flue_sum_molefrac,6)
    flue_massflow_total = my_format(flue_massflow_total,6)
    flue_moleflow_total = my_format(flue_moleflow_total,6)
    
    print('FLUEGAS          |')    
    print('massfrac [-]     |', end = '')    
    for value in flue_maf_conv:
         print("{0:>7}".format(value), end = '')
    print("{0:>7}".format(flue_sum_massfrac))

    print('molefrac [-]     |', end = '')    
    for value in flue_mof_conv:
        print("{0:>7}".format(value), end = '')
    print("{0:>7}".format(flue_sum_molefrac))
    
    print('massflow [kg/s]  |', end = '')    
    for value in flue_mafl_conv:
        print("{0:>7}".format(value), end = '')  
    print("{0:>7}".format(flue_massflow_total))
    
    print('moleflow [mol/s] |', end = '')    
    for value in flue_mofl_conv:
        print("{0:>7}".format(value), end = '')   
    print("{0:>7}".format(flue_moleflow_total))  
    print('\n')
#---------------------------------------------------------------------------------------------------------------
    print('ELEMENTS         |', end ='')
    for value in elem:
        print("{0:>10}".format(value), end = '')
    print('                                 ')
#---------------------------------------------------------------------------------------------------------------    
    fuel_el_moleflow = [0] * len(elem)
    fuel_el_moleflow_conv = []
    fuel_el_moleflow[0] = np.dot(fuel_moleflow_comp, num_C)
    fuel_el_moleflow[1] = np.dot(fuel_moleflow_comp, num_H)
    fuel_el_moleflow[2] = np.dot(fuel_moleflow_comp, num_O)
    fuel_el_moleflow[3] = np.dot(fuel_moleflow_comp, num_S)
    fuel_el_moleflow[4] = np.dot(fuel_moleflow_comp, num_N)
    fuel_el_moleflow[5] = np.dot(fuel_moleflow_comp, num_Ar)
    
    for element in fuel_el_moleflow: 
        fuel_el_moleflow_conv.append(my_format(element,6))   
          
    print('Fuel    [mole/s] |    ', end = '')
    
    for value in fuel_el_moleflow_conv:
         print("{0:10}".format(value), end = '')
    print('                                 ')
#--------------------------------------------------------------------------------------------------------------
    air_el_moleflow = [0] * len(elem)
    air_el_moleflow_conv = []
    air_el_moleflow[0] = np.dot(air_moleflow_comp, num_C)
    air_el_moleflow[1] = np.dot(air_moleflow_comp, num_H)
    air_el_moleflow[2] = np.dot(air_moleflow_comp, num_O)
    air_el_moleflow[3] = np.dot(air_moleflow_comp, num_S)
    air_el_moleflow[4] = np.dot(air_moleflow_comp, num_N)
    air_el_moleflow[5] = np.dot(air_moleflow_comp, num_Ar)
    
    for element in air_el_moleflow: 
        air_el_moleflow_conv.append(my_format(element,6))   
          
    print('Air     [mole/s] |    ', end='')
    
    for value in air_el_moleflow_conv:
         print("{0:10}".format(value), end = '')
    print('                                 ')    
#-------------------------------------------------------------------------------------------------------------
    flue_el_moleflow = [0] * len(elem)
    flue_el_moleflow_conv = []
    flue_el_moleflow[0] = np.dot(flue_moleflow_comp, num_C)
    flue_el_moleflow[1] = np.dot(flue_moleflow_comp, num_H)
    flue_el_moleflow[2] = np.dot(flue_moleflow_comp, num_O)
    flue_el_moleflow[3] = np.dot(flue_moleflow_comp, num_S)
    flue_el_moleflow[4] = np.dot(flue_moleflow_comp, num_N)
    flue_el_moleflow[5] = np.dot(flue_moleflow_comp, num_Ar)
    
    for element in flue_el_moleflow: 
        flue_el_moleflow_conv.append(my_format(element,6))   
          
    print('Flue    [mole/s] |    ', end='')
    
    for value in flue_el_moleflow_conv:
         print("{0:10}".format(value), end = '')
    print('                                 ')    
#----------------------------------------------------------------------------------------------------------------        
    bal_el_moleflow = np.array(air_el_moleflow) + np.array(fuel_el_moleflow) - np.array(flue_el_moleflow)
    bal_el_moleflow_conv = []    
    for element in bal_el_moleflow: 
        bal_el_moleflow_conv.append(my_format(element,6))   
          
    print('Balance [mole/s] |    ', end='')
    
    for value in bal_el_moleflow_conv:
         print("{0:10}".format(value), end = '')
    print('                                                               ',end='\n')       
#-------------------------------------------------------------------------------------------------------------------
    air_temp = air._get_temp()
    air_pressure = air._get_pressure() 
    air_rel_Humid = air._get_rel_Humid()
    
    dry_air_massfrac = air._get_dryair_massfrac()
    dry_air_massfrac_conv = []
    for element in dry_air_massfrac: 
        dry_air_massfrac_conv.append(my_format(element,6)) 
    dry_air_massfrac_sum = my_format(np.sum(dry_air_massfrac),6)
    
    add_air = comb._get_add_air()
    lamb_user = comb._get_lamb_user()
    lamb_comb = comb._get_lamb_comb()    
#--------------------------------------------------------------------------------------------------------------------
    if add_air == True:
        if lamb_comb < 1:
            print('\n')
            print('Calculation for lambda < 1 assumes no formation of CO which is far from reality!')
        if fuel_massfrac[comp.index('O2')] != 0:
            #print('\n')
            print('You have specified Oxygen in fuelgas. The calculation takes this Oxygen into account.')
            
        print('\n')
        print('PARAMETERS       |', end='')
        for value in comp:
            print("{0:>7}".format(value),end='')
        print("{0:>7}".format('SUM'))
  
        print('Dry Air[massfrac]|', end='')
        for value in dry_air_massfrac_conv:
            print("{0:>7}".format(value), end = '')  
        print("{0:>7}".format(dry_air_massfrac_sum), end = '')
        
        print('\n')
        print('Air Temp.     [K] =',air_temp)
        print('Air Pressure  [Pa] =', air_pressure)
        print('Air Rel.Humid.[%/100] =',air_rel_Humid)
        print('lambda        [-] =', lamb_comb)
    elif add_air == False:
        print('\n')
        print('You have specified Oxygen in fuelgas. The lambda value you have specified would require')
        print('-either the amount of Oxygen contained in fuelgas')
        print('-or less Oxygen as contained in fuelgas')
        print('Therefore, the calculation uses Oxygen in fuelgas only and sets the airflow to 0.')
        if lamb_comb < 1:
            print('\n')
            print('Calculation for lambda < 1 assumes no formation of CO which is far from reality!')      
        print('\n')            
        print('PARAMETERS       ')
        print('lambda specified [-] =', lamb_user)
        print('lambda used [-] =', np.around(lamb_comb,3))
        


    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        