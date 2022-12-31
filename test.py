
# インポート
import pandas as pd
from sklearn.datasets import load_boston
import numpy as np
from pandas.plotting import scatter_matrix as mtr
import matplotlib.pyplot as plt

# ボストンの住宅価格データ取得
boston = load_boston()

# データフレーム作成（data = データの順番、columns = ラベル名）
df = pd.DataFrame(boston.data, columns=boston.feature_names)
# 全データ出力

# 条件抽出
updated_data = df.loc[(df["CRIM"] >= 0.05) | ~(df["NOX"] <= 0.5) ,:]

df.to_csv('C:/Users/small/OneDrive/デスクトップ/Excel/komori.csv', header=True,)

# 目的関数をデータフレームに結合する
df['PRICE'] = np.array(boston.target)
print('\n')
print('\n')

# pandasのscatter_matrix関数を用いてペアプロットを出力
fig = pd.plotting.scatter_matrix(df, figsize=(15, 15), grid=True)




print(df)