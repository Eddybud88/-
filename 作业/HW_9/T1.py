import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5],
    'Age': [25, 30, 35]
})

# 使用 merge 函数
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("使用 merge 函数连接的 DataFrame:")
print(merged_df)

print("\n" + "="*40 + "\n")

# 使用 concat 函数（按行拼接）
concat_df_rows = pd.concat([df1, df2], axis=0, ignore_index=True)
print("使用 concat 函数（按行拼接）连接的 DataFrame:")
print(concat_df_rows)

print("\n" + "="*40 + "\n")

# 使用 concat 函数（按列拼接）
concat_df_cols = pd.concat([df1, df2], axis=1)
print("使用 concat 函数（按列拼接）连接的 DataFrame:")
print(concat_df_cols)
