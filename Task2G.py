from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import towns_most_at_risk


def run():
    """Requirements for Task 2G"""
    stations = build_station_list()[:25]
    update_water_levels(stations)
    print(towns_most_at_risk(stations, 10))


if __name__ == '__main__':
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
