
# �C���|�[�g
import pandas as pd
from sklearn.datasets import load_boston
import numpy as np
from pandas.plotting import scatter_matrix as mtr
import matplotlib.pyplot as plt

# �{�X�g���̏Z��i�f�[�^�擾
boston = load_boston()

# �f�[�^�t���[���쐬�idata = �f�[�^�̏��ԁAcolumns = ���x�����j
df = pd.DataFrame(boston.data, columns=boston.feature_names)
# �S�f�[�^�o��

# �������o
updated_data = df.loc[(df["CRIM"] >= 0.05) | ~(df["NOX"] <= 0.5) ,:]

df.to_csv('C:/Users/small/OneDrive/�f�X�N�g�b�v/Excel/komori.csv', header=True,)

# �ړI�֐����f�[�^�t���[���Ɍ�������
df['PRICE'] = np.array(boston.target)
print('\n')
print('\n')

# pandas��scatter_matrix�֐���p���ăy�A�v���b�g���o��
fig = pd.plotting.scatter_matrix(df, figsize=(15, 15), grid=True)




print(df)