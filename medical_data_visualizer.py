import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
def isOverweight(bmi):
    if bmi > 25:
        return 1
    else:
        return 0

# Compute BMI and code if overweight or not
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(isOverweight)

# 3
# Normalize column values, 0=Good 1=Bad

def ternaryToBinary(n):
    if n == 1:
        return 0
    else:
        return 1

df['cholesterol'] = df['cholesterol'].apply(ternaryToBinary)
df['gluc'] = df['gluc'].apply(ternaryToBinary)



# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6
    df_cat = df_cat[['cardio','variable','value']].groupby(['cardio','variable']).value_counts()

    # 7

    # Convert data to long format
    df_cat = df_cat.reset_index()
    df_cat = df_cat.rename(columns={0: 'count'})

    # Graph in seaborn
    cat_plot = sns.catplot(data=df_cat, x="variable", y="count", hue="value", kind="bar", col="cardio", legend="auto")
    cat_plot.set_xlabels('value')
    cat_plot.set_ylabels('total')

    # 8
    fig = cat_plot.figure
    
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
