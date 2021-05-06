import pandas as pd
from lambdata_jcaldwell import helper_functions as hf


# Set path to data
data_path = '/data/country_vacinations_by_manufacturer.csv'

df = pd.read_csv(data_path)
print(df.head())