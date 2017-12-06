import pandas as pd

df_train = pd.read_csv('./train.tsv', sep='\t')
df_test = pd.read_csv('./test.tsv', sep='\t')
print(df_train.shape)
print(df_train.head)
