#!/bin/python3

from learning.dataset import read_csv_dataset, rename_dataframe_columns

df = read_csv_dataset("./corpus/SMSSpamCollection")
df = rename_dataframe_columns(df, (0, 'target'), (1, 'text'))
print(df.head())
