from CoolProp.CoolProp import HAPropsSI
import numpy as np

from back.stream import Stream
from back.block import Block

class HAStreamCreator:
    def __init__(self):
        self.__block = Block().get_block()

    def from_rel_humid(self, dry_air, phi, press, temp):
        
        try: mass_load = HAPropsSI('W','T',temp,'P',press,'R',phi)
        except Exception as e: return str(e)
        
        mass_pct = 100 * mass_load / ( 1 + mass_load )
        
        dry_air_mass_pct_list = dry_air.get_compos('mass_pct_list')
        rest = [100-mass_pct] * len(dry_air_mass_pct_list)
        dummy = np.array(rest) * np.array(dry_air_mass_pct_list) / 100
        
        dummy[self.__block.index('Water')]=mass_pct

        humid_air = Stream()
        humid_air.set_compos(mass_pct_list = list(dummy))

        return humid_air

    def from_mass_pct(self, dry_air, mass_pct, press, temp):
        try: rel_humid = HAPropsSI('R','T',temp,'P',press,'W', mass_pct/(100-mass_pct))
        except Exception as e: return str(e)

        dry_air_mass_pct_list = dry_air.get_compos('mass_pct_list')
        rest = [100-mass_pct] * len(dry_air_mass_pct_list)
        dummy = np.array(rest) * np.array(dry_air_mass_pct_list) / 100
        
        dummy[self.__block.index('Water')]=mass_pct

        humid_air = Stream()
        humid_air.set_compos(mass_pct_list = list(dummy))

        return humid_air
    
    def from_mass_load(self, dry_air, mass_load, press, temp):
        try: rel_humid = HAPropsSI('R','T',temp,'P',press,'W',mass_load)
        except Exception as e: return str(e)

        mass_pct = 100 * mass_load / (1 + mass_load)
        dry_air_mass_pct_list = dry_air.get_compos('mass_pct_list')
        rest = [100-mass_pct] * len(dry_air_mass_pct_list)
        dummy = np.array(rest) * np.array(dry_air_mass_pct_list) / 100
        
        dummy[self.__block.index('Water')] = mass_pct

        humid_air = Stream()
        humid_air.set_compos(mass_pct_list = list(dummy))

        return humid_air
        
    def from_mole_pct(self, dry_air, mole_pct, press, temp):
        try: rel_humid = HAPropsSI('R','T',temp,'P',press,'Y', mole_pct / 100)
        except Exception as e: return str(e)

        dry_air_mole_pct_list = dry_air.get_compos('mole_pct_list')
        rest = [100-mole_pct] * len(dry_air_mole_pct_list)
        dummy = np.array(rest) * np.array(dry_air_mole_pct_list) / 100

        dummy[self.__block.index('Water')]=mole_pct

        humid_air = Stream()
        humid_air.set_compos(mole_pct_list = list(dummy))

        return humid_air

    def from_mole_load(self, dry_air, mole_load, press, temp):
        try: rel_humid = HAPropsSI('R','T',temp,'P',press,'Y', mole_load / (1 + mole_load))
        except Exception as e: return str(e)

        mole_pct = 100 * mole_load / (1 + mole_load)
        dry_air_mole_pct_list = dry_air.get_compos('mole_pct_list')
        rest = [100-mole_pct] * len(dry_air_mole_pct_list)
        dummy = np.array(rest) * np.array(dry_air_mole_pct_list) / 100

        dummy[self.__block.index('Water')] = mole_pct

        humid_air = Stream()
        humid_air.set_compos(mole_pct_list = list(dummy))

        return humid_air





