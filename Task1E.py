from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1E"""
    # Build list of stations
    stations = build_station_list()

    # Get the top 9 rivers by station number
    by_station_number = rivers_by_station_number(stations, 9)

    # When testing, this only gives 9 rivers, as the current list of stations differs from the original list.
    # N=10 gives 11 items.
    print(by_station_number)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
