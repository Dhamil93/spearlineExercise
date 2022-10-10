# spearlineExercise
This is my submission for the Spearline Python Assessment using OpenWeatherAPI

## Running the code
* Open a terminal with path to where the code is saved
* Run command `python` to open the python CLI
* Import the test.py code into the CLI by running `import test`
### Biggest Difference
This function takes in a list of locations and returns the locations with the biggest difference in current temperature, as well as the delta
* Initialise and declare a list of countries you want to get the biggest difference of. It would look something like:
> `list=[<country1>, <country2>, ...]`
* Run the biggest difference of the list using the function `test.biggest_dif(list)` where `list` is your initialised/declared list of countries


Your terminal should look something like this when run:
![img.png](img.png)

### Weather Report for a Location
This function takes in a location and a filename(.csv) and writes a spreadsheet containing  5-day forecast of minimum and maximum temperatures at a 3-hour interval.
* Run the weather report function using `test.weather_report(location, filename)`
