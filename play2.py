from back import Stream
from back import Stream_heat
from back import Combustion

stream_fuel = Stream()
stream_oxgas = Stream()
stream_heat = Stream_heat()

comb = Combustion(lamb=1, stream_fuel=stream_fuel, stream_oxgas=stream_oxgas, stream_heat=stream_heat)
print(comb)
comb.calculate()
print(stream_heat)