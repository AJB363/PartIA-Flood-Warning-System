from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""
    # Build list of stations
    stations = build_station_list()

    # Sort the stations by distance from cambridge centre
    by_river = stations_by_river(stations)

    # Print the closest and furthest 10
    print(sorted(by_river)[:10])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
