def calc_not_given_data(flag1,param1,flag2,param2,comp_molar_weight):
    import numpy as np
    
    def convert_fraction(comp,comp_molar_weight,string):
        if string == 'molefrac_to_massfrac':
            temp_skalar = np.dot(comp,comp_molar_weight)
            temp_vektor = (np.array(comp) * np.array(comp_molar_weight)) / temp_skalar
            return temp_vektor
        elif string == 'massfrac_to_molefrac':
            temp_skalar = np.sum(np.divide(comp,comp_molar_weight))   
            temp_vektor = np.divide(comp,comp_molar_weight)     
            return temp_vektor / temp_skalar
        else:
            raise ValueError 
  
    if flag1 == 'massfrac' and flag2 == 'massflow_total':
        massfrac = param1
        massflow_total = param2
        massflow_comp = massflow_total * np.array(massfrac)
        moleflow_comp = np.divide(massflow_comp,comp_molar_weight)
        moleflow_total = np.sum(moleflow_comp)
        molefrac = np.array(moleflow_comp) / moleflow_total
    elif flag1 == 'massfrac' and flag2 == 'moleflow_total':
        massfrac = param1
        moleflow_total = param2
        molefrac = convert_fraction(massfrac,comp_molar_weight,'massfrac_to_molefrac')
        moleflow_comp = moleflow_total * np.array(molefrac)
        massflow_comp = np.array(moleflow_comp) * np.array(comp_molar_weight)
        massflow_total = np.sum(massflow_comp)
    elif flag1 == 'massfrac' and flag2 == 'none':
        massfrac = param1
        molefrac = convert_fraction(massfrac,comp_molar_weight,'massfrac_to_molefrac')
        massflow_comp = [0] * len(param1)
        moleflow_comp = [0] * len(param1)
        massflow_total = 0.0
        moleflow_total = 0.0
    elif flag1 == 'molefrac' and flag2 == 'massflow_total':
        molefrac = param1
        massflow_total = param2
        massfrac = convert_fraction(molefrac,comp_molar_weight,'molefrac_to_massfrac')
        massflow_comp = massflow_total * np.array(massfrac)
        moleflow_comp = np.divide(massflow_comp, comp_molar_weight)
        moleflow_total = np.sum(moleflow_comp)
    elif flag1 == 'molefrac' and flag2 == 'moleflow_total':
        molefrac = param1
        moleflow_total = param2
        moleflow_comp = param2 * np.array(molefrac) 
        massflow_comp = np.array(comp_molar_weight) * np.array(moleflow_comp)
        massflow_total = np.sum(massflow_comp)
        massfrac = np.array(massflow_comp) / massflow_total
    elif flag1 == 'molefrac' and flag2 == 'none':
        molefrac = param1
        massfrac = convert_fraction(molefrac,comp_molar_weight,'molefrac_to_massfrac')
        massflow_comp = [0] * len(param1)
        moleflow_comp = [0] * len(param1)
        massflow_total = 0.0
        moleflow_total = 0.0
    elif flag1 == 'massflow_comp' and flag2 == 'none':
        massflow_comp = param1
        massflow_total = np.sum(massflow_comp)
        massfrac =  np.array(massflow_comp) / massflow_total
        moleflow_comp = np.divide(massflow_comp,comp_molar_weight)
        moleflow_total = np.sum(moleflow_comp)
        molefrac = np.array(moleflow_comp) / moleflow_total 
    elif flag1 == 'moleflow_comp' and flag2 == 'none':
        moleflow_comp = param1
        moleflow_total = np.sum(moleflow_comp)
        molefrac = np.array(moleflow_comp) / moleflow_total
        massflow_comp = np.array(comp_molar_weight) * np.array(moleflow_comp)
        massflow_total = np.sum(massflow_comp)
        massfrac = np.array(massflow_comp) / massflow_total
    else: 
        raise ValueError
    return [massfrac, molefrac, massflow_comp, moleflow_comp, massflow_total, moleflow_total]

