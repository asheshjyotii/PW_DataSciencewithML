import seaborn as sea

x = sea.get_dataset_names()
print(x) #list of available dataset in seaborn

df =  sea.load_dataset("tips")
print(type(df)) # so sea returns a pandas dataframe

dataset_overview = df.head(5)
print(dataset_overview)# overview of the dataset

# Finding covariance using df.cov()

print(df.info()) # to get the overview of different data types of each columns
# As we can see there are some attributes which are not numberic, df.cov() can only process the numeric data so we separate it

numeric_data_filter = df.select_dtypes(include=["float64","int64"]) # this selects the dtypes specified and returns it as dataframe
print(numeric_data_filter)


covariance_seaborn = numeric_data_filter.cov()# finds the covariance
print(covariance_seaborn)
