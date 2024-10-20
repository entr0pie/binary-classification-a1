#!/bin/python3

from typing import Tuple

import pandas as pd


def read_csv_dataset(path: str, sep: str = '\t') -> pd.DataFrame:
    return pd.read_csv(path, sep=sep)


def rename_dataframe_columns(df: pd.DataFrame, *columns: Tuple[int, str]) -> pd.DataFrame:
    column_mapping = {df.columns[index]: new_name for index, new_name in columns if index < len(df.columns)}
    return df.rename(columns=column_mapping)
