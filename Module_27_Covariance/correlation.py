import seaborn as sea

list_of_datasets = sea.get_dataset_names()

df = sea.get_data_home("tips")
print df