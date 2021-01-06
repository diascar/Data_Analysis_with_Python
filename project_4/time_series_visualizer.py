import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date", parse_dates = True)

# Clean data
filt = (df.loc[:, 'value'] >= df.loc[:, 'value'].quantile(0.025)) & (df.loc[:, 'value'] <= df.loc[:, 'value'].quantile(0.975))

df = df.loc[filt, :]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots()
    ax.plot(df)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index = df_bar.index.map(lambda x: x.year)
    df_bar['Month'] = df.index.map(lambda y: y.month_name())
    df_bar = df_bar.reset_index()
    dfg = df_bar.groupby(['date', 'Month'])['value'].mean().reset_index()

    # Draw bar plot
    global sorted_month_names
    sorted_month_names = [i[0] for i in sorted(set(list(list(zip(df.index.map(lambda x: x.month_name()), df.index.map(lambda y: y.month))))), key = lambda z: z[1])]
    fig, ax = plt.subplots(figsize = (14, 7))
    sns.barplot(x = 'date', y = 'value', hue = 'Month', data = dfg, hue_order = sorted_month_names, ax = ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.month_name()[:3] for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14, 7))
    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    sns.boxplot(x = 'month', y = 'value', data = df_box, ax = ax2, order = [i[:3] for i in sorted_month_names])
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    plt.tight_layout()







    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

