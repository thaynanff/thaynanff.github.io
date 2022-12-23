import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date', parse_dates=['date'])

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
     (df['value'] <= df['value'].quantile(0.975))     
]


def draw_line_plot():
    # Draw line plot
  fig = plt.figure(figsize=(16,4), dpi=175)

  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  plt.xlabel('Date')
  plt.ylabel('Page Views')

  plt.gcf()

  plt.plot(df, color='red')

    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
  df_bar = df.copy()


  df_bar['Years'] = df_bar.index.year
  df_bar['Months'] = df_bar.index.month
  
  month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
               'August', 'September', 'October', 'November', 'December']

  
  df_bar = df_bar.groupby(['Years', 'Months'])['value'].mean()
  df_bar = df_bar.unstack()
  
    # Draw bar plot
  
  fig = df_bar.plot.bar(figsize=(15,10)).figure


  plt.xlabel('Years')
  plt.ylabel('Average Page Views')
  plt.legend(title='Months', labels=month_names)


    # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box['month'] = df_box.index.month
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]

  month_names=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)

  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20,5), dpi=150)

  axes[0] = sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
  axes[0].set_xlabel('Year')
  axes[0].set_ylabel('Page Views')
  axes[0].set_title('Year-wise Box Plot (Trend)')
  
  axes[1] = sns.boxplot(data=df_box, x='month', y='value', ax=axes[1])
  axes[1].set_xlabel('Month')
  axes[1].set_ylabel('Page Views')
  axes[1].set_xticklabels(month_names)
  axes[1].set_title('Month-wise Box Plot (Seasonality)')



    # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
