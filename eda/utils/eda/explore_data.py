import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm
import sklearn as sk


def plot_continuous_variables(data, column_name, plots=['distplot', 'CDF', 'box', 'violin'], scale_limits=None, figsize=(20, 8), histogram=True, log_scale=False):
    '''
    Function to plot continuous variables distribution

    Inputs:
        data: DataFrame
            The DataFrame from which to plot.
        column_name: str
            Column's name whose distribution is to be plotted.
        plots: list, default = ['distplot', 'CDF', box', 'violin']
            List of plots to plot for Continuous Variable.
        scale_limits: tuple (left, right), default = None
            To control the limits of values to be plotted in case of outliers.
        figsize: tuple, default = (20,8)
            Size of the figure to be plotted.
        histogram: bool, default = True
            Whether to plot histogram along with distplot or not.
        log_scale: bool, default = False
            Whether to use log-scale for variables with outlying points.
    '''

    data_to_plot = data.copy()
    if scale_limits:
        # taking only the data within the specified limits
        data_to_plot[column_name] = data[column_name][(
            data[column_name] > scale_limits[0]) & (data[column_name] < scale_limits[1])]

    number_of_subplots = len(plots)
    plt.figure(figsize=figsize)
    sns.set_style('whitegrid')
    palette = ["#466F6D", "#987554"]

    for i, ele in enumerate(plots):
        plt.subplot(1, number_of_subplots, i + 1)
        plt.subplots_adjust(wspace=0.25)

        if ele == 'CDF':
            # making the percentile DataFrame for both positive and negative Class Labels
            percentile_values_0 = data_to_plot[data_to_plot.TARGET == 0][[
                column_name]].dropna().sort_values(by=column_name)
            percentile_values_0['Percentile'] = [
                ele / (len(percentile_values_0)-1) for ele in range(len(percentile_values_0))]

            percentile_values_1 = data_to_plot[data_to_plot.TARGET == 1][[
                column_name]].dropna().sort_values(by=column_name)
            percentile_values_1['Percentile'] = [
                ele / (len(percentile_values_1)-1) for ele in range(len(percentile_values_1))]

            plt.plot(percentile_values_0[column_name],
                     percentile_values_0['Percentile'], color='red', label='Non-Defaulters')
            plt.plot(percentile_values_1[column_name],
                     percentile_values_1['Percentile'], color='black', label='Defaulters')
            plt.xlabel(column_name)
            plt.ylabel('Probability')
            plt.title('CDF of {}'.format(column_name))
            plt.legend(fontsize='medium')
            if log_scale:
                plt.xscale('log')
                plt.xlabel(column_name + ' - (log-scale)')

        if ele == 'distplot':
            sns.distplot(data_to_plot[column_name][data['TARGET'] == 0].dropna(),
                         label='Non-Defaulters', hist=False, color='red')
            sns.distplot(data_to_plot[column_name][data['TARGET'] == 1].dropna(),
                         label='Defaulters', hist=False, color='black')
            plt.xlabel(column_name)
            plt.ylabel('Probability Density')
            plt.legend(fontsize='medium')
            plt.title("Dist-Plot of {}".format(column_name))
            if log_scale:
                plt.xscale('log')
                plt.xlabel(f'{column_name} (log scale)')

        if ele == 'violin':
            sns.violinplot(x='TARGET', y=column_name, data=data_to_plot)
            plt.title("Violin-Plot of {}".format(column_name))
            if log_scale:
                plt.yscale('log')
                plt.ylabel(f'{column_name} (log Scale)')

        if ele == 'box':
            sns.boxplot(x='TARGET', y=column_name,
                        data=data_to_plot, palette=palette)
            plt.title("Box-Plot of {}".format(column_name))
            if log_scale:
                plt.yscale('log')
                plt.ylabel(f'{column_name} (log Scale)')

    plt.show()


def plot_categorical_bar(column_name, data, rotation=0):

    unique_categories_count = data[column_name].value_counts()
    data_values = unique_categories_count.values

    print('-' * 100)
    print(f'The unique categories of {column_name} are:')
    print(unique_categories_count)
    print('-' * 100)
    print(
        f'Total Number of unique categories of {column_name} = {len(unique_categories_count)}')

    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.set(style='whitegrid', font_scale=1.2)

    sns.barplot(ax=axes[0], x=unique_categories_count.index,
                y=unique_categories_count.values, palette='Set1')
    axes[0].set_title(f'Distribution of {column_name}')
    for p in axes[0].patches:
        x, y = p.get_xy()
        height, width = p.get_height(), p.get_width()

        axes[0].annotate(xy=(x + width/3, y + height+100),
                         text=f"{height * 100/sum(data_values) : .2f}%", size=12)

    plt.xticks(rotation=rotation)
    palette = "#2B1125"

    percentage_defaulter_per_category = data[data.TARGET == 1][column_name].value_counts(
    ) * 100 / data[column_name].value_counts()
    percentage_defaulter_per_category.dropna(inplace=True)
    percentage_defaulter_per_category = percentage_defaulter_per_category.round(
        2)

    axes[1] = sns.barplot(ax=axes[1], x=percentage_defaulter_per_category.index,
                          y=percentage_defaulter_per_category.values)

    axes[1].set_title(
        f'Percentage Defaulters in each category of {column_name}')
    axes[1].set_yticklabels(
        [str(label) + '%' for label in axes[1].get_yticks()])
    plt.xticks(rotation=rotation)
    plt.show()
    print('-' * 100)


def plot_categorical_pie(df, labels=None, title=None):

    slice_proportion = dict(df.value_counts(normalize=True))

    pie_chart_colors = cm.get_cmap('Set2')(np.arange(len(slice_proportion)))

    # Set the autopct parameter to display the percentage of each slice next to it
    fig, ax = plt.subplots(figsize=(9, 6))

    # Move ax.pie() outside of the if labels: block
    ax.pie(slice_proportion.values(), labels=labels or slice_proportion.keys(),
           autopct='%.1f%%', startangle=110, colors=pie_chart_colors)

    if title:
        plt.title(title, size=15)

    plt.legend()
    plt.show()
