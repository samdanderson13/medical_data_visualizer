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
    cat_plot.set_xlabels('variable')
    cat_plot.set_ylabels('total')

    # 8
    fig = cat_plot.figure
    
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    height_filter = (df['height'] >= df['height'].quantile(0.025))
    height_filter &= (df['height'] <= df['height'].quantile(0.975))

    weight_filter = (df['weight'] >= df['weight'].quantile(0.025))
    weight_filter &= (df['weight'] <= df['weight'].quantile(0.975))

    bp_filter = (df['ap_lo'] <= df['ap_hi'])

    data_filter = height_filter & weight_filter & bp_filter
    df_heat = df.loc[data_filter]

    # 12
    corr = df_heat.corr()
    corr = corr.round(decimals=1)

    # 13
    length = corr.index.size
    mask = np.fromfunction(lambda i, j: i <= j, (length,length), dtype=int)

    # 14
    fig, ax = plt.subplots(figsize=(8,7))

    # 15

    sns.heatmap(corr, annot=True, linewidth=0.5, mask=mask, ax=ax, square=True, fmt=".1f")
    #fig.subplots_adjust(top=0.95, bottom=0.13)



    # 16
    fig.savefig('heatmap.png')
    return fig
    
