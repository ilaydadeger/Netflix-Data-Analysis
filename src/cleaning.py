import pandas as pd

def clean_netflix_data(df):
    """
    Netflix veri setini temizler ve feature engineering uygular.
    """
    df = df.copy()

    # Tarih formatı
    df['date_added'] = pd.to_datetime(df['date_added'])

    # Eksik veriler
    df['country'] = df['country'].fillna("Unknown")
    df['director'] = df['director'].fillna("Unknown")

    # Süre değerlerini ayır
    df['duration_int'] = df['duration'].str.extract('(\d+)').astype(float)
    df['duration_type'] = df['duration'].str.extract('([a-zA-Z]+)')

    return df
