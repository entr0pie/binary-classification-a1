#!/bin/python3

from learning.dataset import read_csv_dataset, rename_dataframe_columns, split_dataset
from learning.metrics import check_dataframe_balancing

df = read_csv_dataset("./corpus/SMSSpamCollection")
df = rename_dataframe_columns(df, (0, 'target'), (1, 'text'))

balancing = check_dataframe_balancing(df)

X, y = df['text'], df['target']
X_train, X_test, y_train, y_test = split_dataset(X, y)
