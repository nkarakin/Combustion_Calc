class Stream_heat:
    def __init__(self):
        self.__heatflow = None
    def __repr__(self):
        print('heat_flow [W] = ', self.__heatflow)
        return 'Initializing: stream_heat = Stream_heat() / use set-method to set heatflow \n'

    def set_heatflow(self, heatflow):
        self.__heatflow = heatflow
    def get_heatflow(self):
        return self.__heatflow
