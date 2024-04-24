# gdsc-submission
This project is designed to help individuals in Charlottesville assess and optimize their commuting choises in terms of environmental impact and cost efficiency. It calculates the emissions and costs associated with different modes of transportation between any two locations provided by the user. In turn, we hope it encourages users to switch from higher polluting modes of transportion (i.e., gas car) to lesser ones (i.e., biking, walking, public transport, electric car). The project aligns with the following UN Sustainable Development goals
* 11: Sustainable Cities and Communities
* 12: Responsible Consumption and Production
* 13: Climate Action

When the program is run, the user will be prompted to input any two locations, and the program will use Nominatim API to validate and geolocate these locations. The program will calculate the approximate distance between these locations based on geographical coordinates, and will estimate emissions for CO2, NOx, and PM2.5, helping users understand the environmental impact of their commute. Additionally, the program calculates the cost of commuting by car, electric car, bus, and bike, encouraging users to consider cost-effective options.

The following libraries were used:
* math: functions like sqrt and pow used for distance calculations
* geopy: geocoding locations and accessing Nominatim service to validate input locations
* Nominatim: tool that converts location text into geographic coordinates and vice versa.

Use the following to run the program
```
pip install geopy # if not already installed
python sustainable_commute.py
```
