import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv('pokemon_alopez247.csv')

df = df[['isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed','Color','Egg_Group_1','Height_m','Weight_kg','Body_Style']]

df['isLegendary'] = df['isLegendary'].astype(int)

def dummy_creation(df, dummy_creation):
    for i in dummy_creation:
        df_dummy = pd.get_dummies(df[i])
        df = pd.concat([df,df_dummy],axis=1)
        df = df.drop(i, axis=1)
    return(df)
# Essa função pega o dataframe cria uma nova coluna para cada variavel que temos uma coluna para agua que seria 1 se fosse pokemon 
# de agua e 0 se não fosse assim por diante haveria outra coluna para fogo e que seria 1 se um pokemon fosse de fogo  e assim por diante  #
#   pd.get_dummies crua yn dataframe ficticio  e concat concatena no data frame original    # 
