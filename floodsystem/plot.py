import matplotlib.pyplot as plt
import matplotlib.dates as d
from numpy import linspace
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):
    """ Plots the station water level history against time """

    # Return early if data is invalid
    if len(dates) != len(levels):
        print("floodsystem.plot.py plot_water_levels: len(dates) != len(levels)")
        return

    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title('Station: {}'.format(station.name))

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """ Plots the station water level history against time, with a polynomial line of best fit of order p. """

    # Return early if data is invalid
    if len(dates) != len(levels):
        print("floodsystem.plot.py plot_water_levels: len(dates) != len(levels)")
        return

    poly, d0 = polyfit(dates, levels, p)
    x = linspace(0, d.date2num(dates[-1]) - d.date2num(d0), len(dates))

    plt.plot(dates, levels)
    plt.plot(dates, poly(x))

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title('Station: {}'.format(station.name))

    plt.tight_layout()
    plt.show()
