import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2F"""

    # Build a list of the top 5 stations by current water level
    stations = build_station_list()
    update_water_levels(stations)
    top_5_stations = sorted([s for s in stations if s.latest_level is not None],
                            key=lambda x: x.latest_level,
                            reverse=True)[:5]

    # Plot the station levels against time for those stations, for the past 10 days
    dt = datetime.timedelta(days=2)
    for station in top_5_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_level_with_fit(station, dates, levels, 3)


if __name__ == '__main__':
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
