import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18,6))
    df.plot(ax = ax, color='red', linewidth=1)
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')
    ax.tick_params(axis = 'x', labelrotation = 0)
    ax.get_legend().remove()

    fig = plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Completo el rango de meses faltantes para completar el 2016 (solo así categoriza por año)
    anio_completo = pd.date_range("2016-01-01", "2019-12-31")
    df_bar = df_bar.reindex(anio_completo, fill_value = np.nan)
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    df_bar = df_bar.groupby(["year", "month"]).mean()

  # * Completar los valores NaN con 0 para que aparezcan en el gráfico
  # ! Nota: No hacer ésto antes de calcular el promedio o incorporará los valores 0 que pusimos para completar el 2016 como
  # parte del cálculo del promedio (dividiría la suma de los valores del 2016 por 12 meses cuando no hay 12 meses de registro)

    df_bar = df_bar.reset_index().fillna(0.0)

    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(9, 7))
    mes_orden = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    df_bar_plot = sns.barplot(
        data = df_bar,
        x = "year",
        y = "value",
        hue = "month",
        ax = ax,
        hue_order = mes_orden,
        width = 0.5,
        legend = False,
        palette = sns.color_palette("bright", 12),
    )

    df_bar_plot.legend(labels = mes_orden, title = "Months")

    # Capturo el objeto de la leyenda y hago una iteración entre los meses donde setteo el color en cada símbolo (HANDLES)
    # según la paleta Seaborn para cada elemento en su correspondencia
    legend = df_bar_plot.get_legend()
    for i, month in enumerate(mes_orden):
        legend.legendHandles[i].set_color(sns.color_palette("bright", 12)[i])

    # Configuro las etiquetas nombres de ejes
    df_bar_plot.set_xlabel("Years")
    df_bar_plot.set_ylabel("Average Page Views")


    fig = plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig



def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
