# IndexError: single positional indexer is out-of-bounds

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [11, 14, 16, 18],
    'salary': [175.1, 180.2, 190.3, 210.4],
})

print(df)

print('-' * 50)

row_count = len(df.index)
print(row_count)  # 👉️ 4

column_count = df.shape[1]
print(column_count)  # 👉️ 3