import math

from geopy.geocoders import Nominatim
from geopy.point import Point


def calculate_emissions(distance, mode):
    """Estimate emissions in grams per mile."""
    # Emissions factors for CO2, NOx, and PM2.5 (in grams per mile)
    emissions_factors = {
        'car': {'CO2': 271, 'NOx': 0.437, 'PM2.5': 0.029},
        'electric_car': {'CO2': 123, 'NOx': 0.183, 'PM2.5': 0.015},
        'bus': {'CO2': 89, 'NOx': 1.395, 'PM2.5': 0.1},
        'bike': {'CO2': 0, 'NOx': 0, 'PM2.5': 0}
    }
    # Calculating total emissions for the given distance
    return {pollutant: distance * value for pollutant, value in emissions_factors[mode].items()}


def calculate_cost_savings(distance, mode):
    """Calculate costs associated with each mode of transportation."""
    costs_per_mile = {
        'car': 0.15,  # average cost per mile for gasoline vehicles
        'electric_car': 0.05,  # estimated cost per mile for electric cars (varies based on electricity prices)
        'bus': 0.20,  # average fare per mile for bus (varies by location)
        'bike': 0.01  # negligible costs for bike maintenance
    }
    cost = distance * costs_per_mile[mode]
    return cost


# noinspection PyBroadException
def get_user_input():
    """Prompt user for start and end locations and the distance between them."""
    global endLoc, startLoc
    while True:
        print(
            "Please enter your start and end locations to calculate the environmental impact and cost savings of different transportation modes.")
        start = input("Enter starting location: ")
        end = input("Enter ending location: ")
        startGeo = Nominatim(user_agent="this_app")
        endGeo = Nominatim(user_agent="this_app")
        try:
            startLoc = startGeo.geocode(start)
            endLoc = endGeo.geocode(end)
        except BaseException:
            print("Invalid location entered, please try again.")
            print()
            continue
        else:
            break
    return startLoc, endLoc


def suggest_transportation(start, end):
    distance = math.sqrt(pow(end.latitude - start.latitude, 2) + pow(end.longitude - start.longitude, 2))
    modes = ['car', 'electric_car', 'bus', 'bike']
    all_emissions = {mode: calculate_emissions(distance, mode) for mode in modes}
    costs = {mode: calculate_cost_savings(distance, mode) for mode in modes}

    print(f"\nDistance from {start} to {end}: {distance} miles")
    print("Estimated emissions (grams):")
    for mode, emissions in all_emissions.items():
        print(f"\n{mode.capitalize()} Emissions:")
        for pollutant, amount in emissions.items():
            print(f"  {pollutant}: {amount:.2f} grams")

    print("\nTransportation costs ($):")
    for mode, cost in costs.items():
        print(f"  {mode.capitalize()}: {cost:.2f}")


# Main execution
if __name__ == '__main__':
    start_location, end_location = get_user_input()
    suggest_transportation(start_location, end_location)
