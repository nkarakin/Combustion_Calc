import numpy as np
import pandas as pd
from back import Stream

from back import Block

block_comp = Block().get_block()
air_obj = Stream()
air_obj.set_compos(mass_pct_list = [0, 0, 75.5, 1.3, 23.2, 0, 0, 0, 0, 0, 0, 0])


columns = ['mole%','mass%']
col1 = columns[0].replace('%','') + '_pct_list'
col2 = columns[1].replace('%','') + '_pct_list'

arr = np.array([air_obj.get_compos(col1),air_obj.get_compos(col2)])
arrT = arr.T
df = pd.DataFrame(arrT,index = block_comp, columns = columns)
print(df)

