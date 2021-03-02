import numpy as np
import matplotlib.dates as d


def polyfit(dates, levels, p):
    """ Finds the polynomial of degree p that best fits the graph of levels against dates. """

    if len(levels) != len(dates):
        return False, False
    if len(dates) == 0:
        return False, False

    dates_f = d.date2num(dates)

    # Sets x_0 to 0
    d0_f = dates_f[0]
    d0 = d.num2date(d0_f)

    poly = np.poly1d(np.polyfit(dates_f - d0_f, levels, p))

    return poly, d0
