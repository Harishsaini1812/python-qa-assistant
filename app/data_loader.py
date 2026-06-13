import pandas as pd

def load_data(path="data/Questions.csv", encoding="utf-8"):
    df = pd.read_csv(path)

    # Safe columns handling
    df = df[['Title', 'Body']].dropna()

    # Combine title + body
    df['text'] = df['Title'] + "\n" + df['Body']

    return df['text'].tolist()