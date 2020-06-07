class Block:
    def __init__(self):
        import CoolProp.CoolProp as dummy
        self.cp = dummy
                     
        self.__block = ['CarbonDioxide','Water','Nitrogen','Argon','Oxygen','SulfurDioxide','CarbonMonoxide','Hydrogen','Methane','HydrogenSulfide','Ethane','n-Propane']
        self.__elem  = ['C','H','O','S','N','Ar'] # All Elements present in the Block have to be here!
        self.__mw_elem = [0.0120107, 0.00100794, 0.0159994, 0.032065, 0.0140067 , 0.039948]
        self.__drai_mass_pct_list = [0, 0, 75.5, 1.3, 23.2, 0, 0, 0, 0, 0, 0, 0]
        self.__drai_mole_pct_list = [0, 0, 78.1, 0.9, 21.0, 0, 0, 0, 0, 0, 0, 0]

    def get_block(self):
        return self.__block
    def get_elem(self):
        return self.__elem

    def get_mw_block(self):
        comp_molar_weight = []                      
        for element in self.__block:
            comp_molar_weight.append(self.cp.PropsSI('MOLARMASS',element)) 
        return comp_molar_weight
    def get_mw_elem(self):
        return self.__mw_elem


    def get_drai_mass_pct_list(self):
        return self.__drai_mass_pct_list
    def get_drai_mole_pct_list(self):
        return self.__drai_mole_pct_list
    
    # get index or tuple with indexes (!!! start is 1 !!!)
    def index(self,comp):
        return self.__block.index(comp)+1 
    def indexs(self,*args):
        list = []
        for a in args: list.append(self.index(a))
        return tuple(list)


    



