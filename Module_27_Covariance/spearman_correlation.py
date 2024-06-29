#%%
import seaborn as sea

x = sea.get_dataset_names()
print(x) #list of available dataset in seaborn

df =  sea.load_dataset("tips")
print(type(df)) # so sea returns a pandas dataframe

dataset_overview = df.head(5)
print(dataset_overview)# overview of the dataset

# Finding Spearman correlation using df.corr(method="spearman")

print(df.info()) # to get the overview of different data types of each columns
# As we can see there are some attributes which are not numberic, df.corr(method="spearman") can only process the numeric data so we separate it

numeric_data_filter = df.select_dtypes(exclude="category") # this excludes the dtypes specified and returns it as dataframe
print(numeric_data_filter)


correlation_seaborn_pdframe = numeric_data_filter.corr(method="spearman")# finds the Spearman correlation, by default without paramenters df.corr() finds the Spearman correlation
print(correlation_seaborn_pdframe)
#%%
#generating heatmap using seaborn of the spearman_correlation

sea.heatmap(correlation_seaborn_pdframe,annot= True)