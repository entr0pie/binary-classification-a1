#!/bin/python3

import pandas as pd


def check_dataframe_balancing(df: pd.DataFrame, target_column_name: str = 'target') -> pd.DataFrame:
    return df[target_column_name].value_counts(normalize=True)
