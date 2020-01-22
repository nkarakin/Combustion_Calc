from Stream_def import Stream_def
from Stream_def_HA import Stream_def_HA
class Combustion:
    def __init__(self, lamb_user, obj_fuel: Stream_def, obj_air: Stream_def_HA):
        import numpy as np 
#----------------------------------------------------------------------------------------------------------
        block = ['CarbonDioxide','Water','Nitrogen','Argon','Oxygen','SulfurDioxide','CarbonMonoxide','Hydrogen','Methane','HydrogenSulfide','Ethane','n-Propane']
        index_CO2  = block.index('CarbonDioxide')
        index_H2O = block.index('Water')
        index_N2 = block.index('Nitrogen')
        index_Ar = block.index('Argon')
        index_O2 = block.index('Oxygen')
        index_SO2 = block.index('SulfurDioxide') 
        index_CO = block.index('CarbonMonoxide')
        index_H2 = block.index('Hydrogen')
        index_CH4 = block.index('Methane')
        index_H2S = block.index('HydrogenSulfide')
        index_C2H6 = block.index('Ethane')
        index_C3H8 = block.index('n-Propane')
        
        O2_rq =  [0, 0, 0, 0, 0, 0, 0.5, 0.5, 2.0, 1.5, 3.5, 5.0]
        CO2_pr = [0, 0, 0, 0, 0, 0, 1.0, 0.0, 1.0, 0.0, 2.0, 3.0]
        H2O_pr = [0, 0, 0, 0, 0, 0, 0.0, 1.0, 2.0, 1.0, 3.0, 4.0]
        SO2_pr = [0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
        
        if lamb_user < 0 or lamb_user == 0:
            print('lambda has to be greater than zero')
            raise ValueError
        
        fuel_moleflow_comp = obj_fuel.get_moleflow_comp()
        burnables = fuel_moleflow_comp[block.index('CarbonMonoxide'):]
        if np.sum(burnables) == 0:
            print('You have to specify at least one burnable component')
            raise ValueError        
        
        O2_rq_moleflow_total = np.dot(fuel_moleflow_comp,O2_rq)
        delta = fuel_moleflow_comp[index_O2] - O2_rq_moleflow_total * lamb_user
        
        if delta < 0: # air stream is required 
            self._add_air = True
            # vektor: air flow (component wise) for given fuel and given lambda [kmole / s]         
            air_molefrac = obj_air.get_molefrac()
            air_moleflow_comp = list(((-1)*delta/air_molefrac[index_O2])*np.array(air_molefrac))
            # with calculatet air flow change the air stream
            obj_air._reset_using_parent_init('moleflow_comp',air_moleflow_comp,'none','none')
            air_moleflow_comp = obj_air.get_moleflow_comp()
            lamb = lamb_user
        else: # air steam is not required
            self._add_air = False
            # change the airstream: fractions = yes, flows = no
            air_molefrac = obj_air.get_molefrac()
            obj_air._reset_using_parent_init('molefrac',list(air_molefrac),'none','none')
            air_moleflow_comp = obj_air.get_moleflow_comp()
            lamb = fuel_moleflow_comp[index_O2]/O2_rq_moleflow_total
        
        flue_moleflow_comp = [None] * len(block)
#----------------------------------------------------------------------------------------------------------        
        if lamb < 1:
            # CO2: air + fuel + CO2_prod * lamb
            flue_moleflow_comp[index_CO2] = \
            air_moleflow_comp[index_CO2] + fuel_moleflow_comp[index_CO2] + np.dot(CO2_pr, fuel_moleflow_comp) * lamb
            # H2O: air + fuel + H2O-prod * lamb
            flue_moleflow_comp[index_H2O] = \
            air_moleflow_comp[index_H2O] + fuel_moleflow_comp[index_H2O] + np.dot(H2O_pr, fuel_moleflow_comp) * lamb
            # N2: air + fuel
            flue_moleflow_comp[index_N2] = \
            air_moleflow_comp[index_N2] + fuel_moleflow_comp[index_N2]
            # Ar: air + fuel
            flue_moleflow_comp[index_Ar] = \
            air_moleflow_comp[index_Ar] + fuel_moleflow_comp[index_Ar]
            # O2: completely consumed 
            flue_moleflow_comp[index_O2]    = 0
            # SO2: air + fuel + SO2_prod * lamb
            flue_moleflow_comp[index_SO2] = \
            air_moleflow_comp[index_SO2] + fuel_moleflow_comp[index_SO2] + np.dot(SO2_pr, fuel_moleflow_comp) * lamb
            # CO: fuel * (1-lamb)
            flue_moleflow_comp[index_CO] = fuel_moleflow_comp[index_CO] * (1-lamb)
            # H2: fuel * (1-lamb)
            flue_moleflow_comp[index_H2] = fuel_moleflow_comp[index_H2] * (1-lamb)
            # CH4: fuel * (1-lamb)
            flue_moleflow_comp[index_CH4] = fuel_moleflow_comp[index_CH4] * (1-lamb)
            # H2S: fuel * (1-lamb)
            flue_moleflow_comp[index_H2S] = fuel_moleflow_comp[index_H2S] * (1-lamb)
            #C2H6: fuel * (1-lamb)
            flue_moleflow_comp[index_C2H6] = fuel_moleflow_comp[index_C2H6] * (1-lamb)
            #C3H8: fuel * (1-lamb)
            flue_moleflow_comp[index_C3H8] = fuel_moleflow_comp[index_C3H8] * (1-lamb)
        else:
            # CO2: air + fuel + CO2_prod 
            flue_moleflow_comp[index_CO2] = \
            air_moleflow_comp[index_CO2] + fuel_moleflow_comp[index_CO2] + np.dot(CO2_pr, fuel_moleflow_comp)
            # H2O: air + fuel + H2O_prod 
            flue_moleflow_comp[index_H2O] = \
            air_moleflow_comp[index_H2O] + fuel_moleflow_comp[index_H2O] + np.dot(H2O_pr, fuel_moleflow_comp)
            # N2: air + fuel
            flue_moleflow_comp[index_N2] = \
            air_moleflow_comp[index_N2] + fuel_moleflow_comp[index_N2]
            # Ar: air + fuel
            flue_moleflow_comp[index_Ar] = \
            air_moleflow_comp[index_Ar] + fuel_moleflow_comp[index_Ar]
            # O2: air + fuel - consumed
            flue_moleflow_comp[index_O2] = \
            air_moleflow_comp[index_O2] + fuel_moleflow_comp[index_O2] - O2_rq_moleflow_total
            # SO2: air + fuel + SO2_prod 
            flue_moleflow_comp[index_SO2] = \
            air_moleflow_comp[index_SO2] + fuel_moleflow_comp[index_SO2] + np.dot(SO2_pr, fuel_moleflow_comp)
            # CO: completely consumed
            flue_moleflow_comp[index_CO] = 0
            # H2: completely consumed
            flue_moleflow_comp[index_H2] = 0
            # CH4: completely consumed
            flue_moleflow_comp[index_CH4] = 0
            # H2S: completely consumed
            flue_moleflow_comp[index_H2S] = 0
            #C2H6: completely consumed
            flue_moleflow_comp[index_C2H6] = 0
            #C3H8: completely consumed
            flue_moleflow_comp[index_C3H8] = 0
                    
        # creation of the flue-stream object: 
        self.__fluegas = Stream_def('moleflow_comp',flue_moleflow_comp,'none','none') 
        
        self._lamb_user = lamb_user
        self._lamb_comb = lamb
    
    def _get_lamb_user(self):
        return self._lamb_user
    def _get_lamb_comb(self):
        return self._lamb_comb           
    def _get_add_air(self):
        return self._add_air        
    def get_fluegas(self):
        return self.__fluegas