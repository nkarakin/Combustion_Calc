from Stream_def import Stream_def

class Stream_def_HA(Stream_def):
    
    def __init__(self, temp, pressure, rel_Humid, dryair_massfrac):
        
        self._temp = temp
        self._pressure = pressure
        self._rel_Humid = rel_Humid
        self._dryair_massfrac = dryair_massfrac
#---------------------------------------------------------------------------------------
        comp_names = ['CarbonDioxide','Water','Nitrogen','Argon','Oxygen','SulfurDioxide','CarbonMonoxide','Hydrogen','Methane','HydrogenSulfide','Ethane','n-Propane']
        
#---------------------------------------------------------------------------------------
        import CoolProp.CoolProp as prop_HA
        import numpy as np        
#---------------------------------------------------------------------------------------                
        if temp < 0 or pressure < 0 or temp == 0 or pressure == 0:
            print('pressure[Pa] and Temperature[K] must be greater than zero')
            raise ValueError     
        elif rel_Humid > 1 or rel_Humid < 0:
            print('Relative Humidity must be between 0 and 1')
            raise ValueError
        else:
            for value in dryair_massfrac:
                a=dryair_massfrac.index(value)
                if dryair_massfrac[a] < 0:
                    print('Component less than zero!')
                    raise ValueError
        
        burnables = dryair_massfrac[comp_names.index('CarbonMonoxide'):]
        if dryair_massfrac[comp_names.index('Water')] != 0:            
            print('Dry air must not contain Water')
            raise ValueError
        elif np.sum(burnables) != 0:
            print('Air must not contain burnable components')
            raise ValueError
        elif dryair_massfrac[comp_names.index('Oxygen')] == 0:
            print('Air must contain Oxygen')
            raise ValueError
#---------------------------------------------------------------------------------------            
        if rel_Humid == 0:
            massfrac_H2O = 0
        else:
            load_H2O = prop_HA.HAPropsSI('W','T',temp,'P',pressure,'R',rel_Humid)
            massfrac_H2O = 1/((1/load_H2O) + 1)
        
        index_H2O = comp_names.index('Water')
        temp_vek = (1-massfrac_H2O) * np.array(dryair_massfrac)        
        temp_vek[index_H2O] = massfrac_H2O
        self.__wetair_massfrac = list(temp_vek)
#----------------------------------------------------------------------------------------        
        super().__init__('massfrac', self.__wetair_massfrac,'none','none')
#----------------------------------------------------------------------------------------
    def _reset_using_parent_init(self,flag1,param1,flag2,param2):
        super().__init__(flag1,param1,flag2,param2)
        
    def _get_temp(self):
        return self._temp
    
    def _get_pressure(self):
        return self._pressure
    
    def _get_rel_Humid(self):
        return self._rel_Humid
        
    def _get_dryair_massfrac(self):
        return self._dryair_massfrac
