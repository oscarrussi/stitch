import pandas as pd

def get_data_as_numpy_array(file, num_columns):
  read_file = pd.read_csv(file)
  df= read_file.iloc[:,0:num_columns]
  return df.to_numpy() # convert dataframe to numpy

# get_data_as_numpy_array("example_clean_data.txt", 2)

