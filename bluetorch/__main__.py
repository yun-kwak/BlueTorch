if '__file__' in globals():
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from bluetorch import Variable

x = Variable(np.array(1.0))
y = Variable(np.array(2.0))
z = x + y
print(z.data)
