# Import numpy as np
import numpy as np
np_height= np.array([74, 74, 72, 75, 75, 73])
np_baseball= np.array([[ 74, 180],[ 74, 215],[ 72, 210],[ 75, 205],[ 75, 190],[ 73, 195]])

# For loop over np_height
for inches in np_height:
    print(str(inches)+" inches")

# For loop over np_baseball
for player in np.nditer(np_baseball):
    print(type(player))