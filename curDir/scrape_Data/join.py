import pandas as pd

# reading two csv files
data1 = pd.read_excel('Master_Sheet.xlsx')
data2 = pd.read_excel('allimages.xlsx')

# using merge function by setting how='inner'
output1 = pd.merge(data1, data2,
				on='ID',
				how='left')

# displaying result
output1.to_excel('Final_MasterSheet.xlsx')
