from back import Block

class Stream:
    #__comp = ['CarbonDioxide','Water','Nitrogen','Argon','Oxygen','SulfurDioxide','CarbonMonoxide','Hydrogen','Methane','HydrogenSulfide','Ethane','n-Propane']
    #__comp = Block.get_block()

    def __init__(self):
        self.__comp = Block().get_block()
        self.__mass_pct_list = []
        self.__mole_pct_list = [] 
        self.__mass_flow = None
        self.__mole_flow = None
        self.__press = None
        self.__temp = None
        self.__h = None

        #import validation as dummy  
        #self.v = dummy.Validation()
        import numpy as dummy
        self.np = dummy
        import CoolProp.CoolProp as dummy
        self.cp = dummy

    def __repr__(self):
        print('mass_pct_list[%] = ', self.__mass_pct_list, '\nmole_pct_list[%] = ', self.__mole_pct_list)
        print('mass_flow[kg/s] = ', self.__mass_flow, '\nmole_flow[mole/s] = ',self.__mole_flow)
        print('press[Pa] = ', self.__press, '\ntemp[K] = ',self.__temp, '\nenthalpy[J/kg-K] = ', self.__h)
        return 'Initializing: stream = Stream() / use set-methods to pass composition, flow, temp, press to the object\n'
 #----------------------------------------------Set - Methods   
    def set_compos(self,**arg):
        if list(arg.keys())[0] == 'mass_pct_list': 
            self.__mass_pct_list = arg.get(list(arg.keys())[0])
            self.__mole_pct_list = self.mass_to_mole(arg.get(list(arg.keys())[0]))
        elif list(arg.keys())[0] == 'mole_pct_list': 
            self.__mole_pct_list = arg.get(list(arg.keys())[0])
            self.__mass_pct_list = self.mole_to_mass(arg.get(list(arg.keys())[0]))
        if self.__mass_pct_list != [] and self.__press != None and self.__temp != None:
            self.__h = self.calc_enthalpy()
    
    def set_flow(self,**arg):
        if list(arg.keys())[0] == 'mass_flow':
            self.__mass_flow = arg.get(list(arg.keys())[0])
            if self.__mass_pct_list != []:
                comp_molar_weight = Block().get_mw_block()
                stream_molar_weight = 0.01 * self.np.dot(comp_molar_weight,self.__mole_pct_list)
                self.__mole_flow = self.__mass_flow / stream_molar_weight
        elif list(arg.keys())[0] == 'mole_flow':
            self.__mole_flow = arg.get(list(arg.keys())[0])
            if self.__mass_pct_list != []:
                comp_molar_weight = Block().get_mw_block()
                stream_molar_weight = 0.01 * self.np.dot(comp_molar_weight,self.__mole_pct_list)
                self.__mass_flow = self.__mole_flow * stream_molar_weight

    def set_press(self,press):
        self.__press = press
        if self.__mass_pct_list != [] and self.__press != None and self.__temp != None:
            self.__h = self.calc_enthalpy()

    def set_temp(self,temp):
        self.__temp = temp
        if self.__mass_pct_list != [] and self.__press != None and self.__temp != None:
            self.__h = self.calc_enthalpy()

 #----------------------------------------------Methods used by above methods  
    def calc_enthalpy(self):
        enthalpy_vector = []
        for element in self.__comp:
            enthalpy_vector.append(self.cp.PropsSI('H','P',self.__press,'T',self.__temp,element))
        return self.np.dot(enthalpy_vector,[x * 0.01 for x in self.__mass_pct_list])

    def mass_to_mole(self,mass_pct_list):
        comp_molar_weight = Block().get_mw_block()
        temp_skalar = self.np.sum(self.np.divide(mass_pct_list,comp_molar_weight))   
        temp_vektor = self.np.divide(mass_pct_list,comp_molar_weight) 
        return  list(100 * (temp_vektor / temp_skalar))
        
    def mole_to_mass(self,mole_pct_list):
        comp_molar_weight = Block().get_mw_block()
        temp_skalar = self.np.dot(mole_pct_list,comp_molar_weight)
        return list(100 * ((self.np.array(mole_pct_list) * self.np.array(comp_molar_weight)) / temp_skalar))

 #----------------------------------------------Get-Methods    
    def get_flow(self,key):
        if key == 'mass_flow': return self.__mass_flow
        elif key == 'mole_flow': return self.__mole_flow
    
    def get_compos(self, key):
        if key == 'mass_pct_list': return self.__mass_pct_list
        elif key == 'mole_pct_list': return self.__mole_pct_list
    
    def get_enthalpy(self):
        return self.__h
        
    
        


