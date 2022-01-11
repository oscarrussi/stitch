# Import cars data
import pandas as pd
cars = pd.read_csv('../cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out third, fourth and fifth observation
print(cars[3:6])