#!/bin/python3

import pandas as pd
from sklearn.model_selection import train_test_split


def split_dataset(
        x: pd.Series,
        y: pd.Series, test_size: float = 0.30,
        random_state: int = 42
) -> (list, list, list, list):
    return train_test_split(x, y, test_size=test_size, random_state=random_state)
