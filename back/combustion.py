class Combustion:
    def __init__(self,**kwargs):
        if 'lamb' in kwargs: self.lamb = kwargs.get('lamb')
        else: self.lamb = None
        if 'stream_fuel' in kwargs: self.stream_fuel = kwargs.get('stream_fuel')
        else: self.stream_fuel = None
        if 'stream_oxgas' in kwargs: self.stream_oxgas = kwargs.get('stream_oxgas')
        else: self.stream_oxgas = None
        if 'stream_heat' in kwargs: self.stream_heat = kwargs.get('stream_heat')
        else: self.stream_heat = None


    def __repr__(self):
        print('Lambda[-] = ', self.lamb,'\n')
        print('Fuel Stream:'); print(self.stream_fuel,'\n')
        print('Oxidation Gas:'); print(self.stream_oxgas,'\n')
        print('Heat Stream:'); print(self.stream_heat,'\n')
        return "Initialization: combustion = Combustion(kwargs) / kwargs are: 'lamb'(number), 'stream_fuel'(stream-obj),'stream_oxgas'(stream-obj), 'stream_heat'(stream_heat-obj). You don't need all of them"
    
    def calculate(self):
        self.stream_heat.set_heatflow(1)
        