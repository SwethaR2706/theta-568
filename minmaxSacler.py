import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'Age': [25, 30, 35, 40, 45],
    'Height': [150, 160, 170, 180, 190],  
    'Weight': [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print("\nNormalized DataFrame (scaled to range [0,1]):")
print(normalized_df)