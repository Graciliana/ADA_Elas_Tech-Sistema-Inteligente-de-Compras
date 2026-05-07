import pandas as pd

def load_inventory():

    return pd.read_parquet(
        'data/processed/intelligent_inventory.parquet'
    )

def load_risk():

    return pd.read_parquet(
        '../data/processed/risk_by_category.parquet'
    )

def load_overstock():

    return pd.read_parquet(
        '../data/processed/overstock_by_category.parquet'
    )