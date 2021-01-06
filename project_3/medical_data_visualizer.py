import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df["weight"]/(df["height"]/100)**2 ).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    rdf = df[['cardio', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']]
    nrdf = rdf.set_index("cardio")
    df_cat = pd.melt(nrdf, ignore_index = False)
    


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat.reset_index(inplace = True)
    var_order = sorted(df_cat.loc[:, "variable"].unique())

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable', hue = 'value', col = 'cardio', data = df_cat, kind = 'count', order = var_order)
    fig.set_axis_labels(y_var = 'total')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    filt = (df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df.loc[filt, :]

    # Calculate the correlation matrix
    corr = np.round(df_heat.corr(), 1)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, annot = True, fmt = '.1f', vmax = 0.3, center = 0.0, ax = ax)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
