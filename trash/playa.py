from back import formater
from back import rand_gen_vec

import pandas as pd
import numpy as np
a = [0,11,9]
b = [formater(x,7,3) for x in a]
print(len(str(b[0])))
ar = np.array([b]).T
df = pd.DataFrame(ar)
print(df)

