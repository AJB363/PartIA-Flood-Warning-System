import matplotlib.pyplot as plt


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
