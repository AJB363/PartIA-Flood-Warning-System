from datetime import timedelta
from .datafetcher import fetch_measure_levels
from .analysis import polyfit


def stations_level_over_threshold(stations, tol):
    '''Return a list of tuples where each tuple holds a station with latest relative'''
    '''water level above tol and the relative water level at the station.'''

    stations_over_threshold = []
    for station in stations:
        if station.typical_range_consistent() is False:
            continue

        try:
            if station.relative_water_level() > tol:
                stations_over_threshold.append((station.name, station.relative_water_level()))
        except Exception:
            continue

    return sorted(stations_over_threshold, key=lambda x: x[1], reverse=True)


def stations_highest_rel_level(stations, N):
    '''Return N number of stations at which the water level relative to the typical range is highest'''

    stations_at_risk = []
    for station in stations:
        try:
            water_level = station.relative_water_level()
            if water_level is not None:
                stations_at_risk.append((station.name, station.relative_water_level()))
        except Exception:
            continue

    return sorted(stations_at_risk, key=lambda x: x[1], reverse=True)[:N]


def towns_most_at_risk(stations, N):
    """Gets a list of length N, if at least N towns exist, of:"""
    """   (towns most at risk, risk severity, next expected relative water level) tuples."""
    """ """
    """   Does not update water levels, please make sure water levels are up to date before calling."""
    """   Can be slow, as it iterates through finding water levels and water level changes for all"""
    """   stations passed in."""

    # degree of polynomial to use for the water level profile
    polynomial_degree = 3

    # number of datapoints used to calculate the gradient average
    gradient_average_points = 5

    # Calculate the current risk level for each station
    stations_most_at_risk = []
    for station in stations:
        # Gets the current station level
        dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=10))

        # Calculates the average gradient at the end of the polynomial for water level
        poly, _ = polyfit(dates, levels, polynomial_degree)
        if not poly:  # if polyfit fails
            continue

        gradient = poly.deriv()
        gradient_len = len(gradient)
        gradient_avg = 0
        for i in range(gradient_average_points):
            gradient_avg += gradient[gradient_len - (1 + i)]
        gradient_avg /= gradient_average_points

        # Estimates the expected relative water height in 1 day
        expected_level = station.latest_level + gradient_avg

        expected_relative_level = 0.0
        if station.typical_range_consistent():
            expected_relative_level = ((expected_level - station.typical_range[0])
                                       / (station.typical_range[1] - station.typical_range[0]))

        # Assigns risk level
        risk = ""
        if expected_relative_level <= 0.5:    # Less than 50% of average maximum water level
            risk = "low"
        elif expected_relative_level <= 1.0:  # 50-100% of average maximum water level
            risk = "moderate"
        elif expected_relative_level <= 1.3:  # 0-30% higher than average maximum water level
            risk = "high"
        else:                                 # >30% higher than average maximum water level
            risk = "severe"

        station_with_risk_level = (station, risk, expected_relative_level)
        stations_most_at_risk.append(station_with_risk_level)

    # Sort the stations by risk level
    stations_most_at_risk = sorted(stations_most_at_risk, key=lambda x: x[2], reverse=True)

    # Get the N towns most at risk
    N_towns_most_at_risk = []
    for station_r in stations_most_at_risk:
        # Early exit if we have enough towns
        if len(N_towns_most_at_risk) >= N:
            break

        # Check if the town is already in the list
        if len(N_towns_most_at_risk) != 0 and station_r[0].town in [t[0] for t in N_towns_most_at_risk]:
            continue

        # Adds the new town to the list, with it's severity and expected relative water level.
        town_risk_profile = (station_r[0].town, station_r[1], station_r[2])
        N_towns_most_at_risk.append(town_risk_profile)

    return N_towns_most_at_risk
