import pandas as pd

df_train = pd.read_csv('./train.tsv', sep='\t')
print(df_train.head())
