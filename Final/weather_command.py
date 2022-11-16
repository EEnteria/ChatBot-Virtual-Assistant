import python_weather
import asyncio
import os
from database import object_type, database

class weather_command(object_type):
	def __init__ (self, name = "weather" , list_of_objects = []):
		database.__init__(self, list_of_objects, name)

	
	def execute(self, args = []):
		location = "New York"
		keywords = ["at", "in"]
		#City Starters to grab the full name
		city_starters = ["ann", "baton", "boca", "broken", "cape", "cedar", "chula", "college", "colorado", "coral", "corpus", "costa", "daytona", "des", "el", "fort", "garden", "grand", "green", "high", "huntington", "jersey", "jurupa", "kansas", "las", "league", "little", "long", "los", "miami", "moreno","new", "north", "oaklahoma", "overland", "palm", "pembroke", "pompano", "rancho", "round", "saint", "san", "sandy", "santa", "simi", "sioux", "south", "spokane", "sterling", "sugar", "thousand", "virginia", "west", "wichita"]
		if len(args) > 0:
			for i in range(0, len(args) - 1):
		                #Checks for the keywords asking for location
					if args[i] in keywords:
					#Grabs city starters if there are any
						if args[i + 1] in city_starters:
							location = args[i + 1] + " " + args[i + 2]
		
						else:
							location = args[i + 1]
	                
	
	
        
		asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

		in_celsius = False
		if "celsius" in args: in_celsius = True
		asyncio.run(self._getweather(location, in_celsius))
            
        
	async def _getweather(self,location, in_celsius):
		if in_celsius: c = python_weather.Client()
		else: c = python_weather.Client(format=python_weather.IMPERIAL)
	
		async with c as client:
			weather = await client.get(location)
			print(weather.current.temperature)
	
			for forecast in weather.forecasts:
				print(forecast.date, forecast.astronomy)
	
			for hourly in forecast.hourly:
				print(f" --> {hourly!r}")
              

           
if __name__ == "__main__":
	test = weather_command()

	test.execute(['in', 'harrisburg', 'celsius'])
	test.execute(['in', 'harrisburg'])