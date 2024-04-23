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






def get_user_input():
   """Prompt user for start and end locations and the distance between them."""
   print("Please enter your start and end locations to calculate the environmental impact and cost savings of different transportation modes.")
   start = input("Enter start location: ")
   end = input("Enter end location: ")
   distance = float(input("Enter the distance between these locations in miles: "))
   return start, end, distance




def suggest_transportation(start, end, distance):
   modes = ['car', 'electric_car', 'bus', 'bike']
   all_emissions = {mode: calculate_emissions(distance, mode) for mode in modes}
   costs = {mode: calculate_cost_savings(distance, mode) for mode in modes}


   print(f"\nDistance from {start} to {end}: {distance} miles")
   print("Estimated emissions (grams):")
   for mode, emissions in all_emissions.items():
