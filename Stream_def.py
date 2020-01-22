class Stream_def:
    def __init__(self,flag1,param1,flag2,param2): 
#----------------------------------------------------------------------------------------        
        comp_names = ['CarbonDioxide','Water','Nitrogen','Argon','Oxygen','SulfurDioxide','CarbonMonoxide','Hydrogen','Methane','HydrogenSulfide','Ethane','n-Propane']
#----------------------------------------------------------------------------------------    
        import catch_errors
        catch_errors.catch_errors(flag1,param1,flag2,param2,len(comp_names))
#----------------------------------------------------------------------------------------               
        import CoolProp.CoolProp as prop
        comp_molar_weight = []                       
        for element in comp_names:
            comp_molar_weight.append(prop.PropsSI('MOLARMASS',element))          
           
        import calc_not_given_data
        self.__data = calc_not_given_data.calc_not_given_data(flag1,param1,flag2,param2,comp_molar_weight)
#----------------------------------------------------------------------------------------  
    def get_massfrac(self):
        return self.__data[0]
    def get_molefrac(self):
        return self.__data[1]
    def get_massflow_comp(self):
        return self.__data[2]
    def get_moleflow_comp(self):
        return self.__data[3]
    def get_massflow_total(self):
        return self.__data[4]
    def get_moleflow_total(self):
        return self.__data[5]


