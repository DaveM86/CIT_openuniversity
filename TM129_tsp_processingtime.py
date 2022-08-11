'''
The travelling salesman problem (TSP) is a well-known problem in AI and robotics.

Show the working used to calculate your answers. Give your answers in everyday units, for example using hours, minutes and seconds as appropriate.

i.An autonomous remote-sensing drone has been given the task of taking images over 14 locations and must plan a route to avoid running out of power.
Treating this as a TSP with the drone starting from one of the locations, how many possible routes might the drone take? Give your answer in scientific notation to 2 decimal places.

ii.If the drone’s on-board computer can process 70 000 000 routes per second, how long would it take it to evaluate every possible solution? Give your answer to 2 significant figures.

iii.A proposed increase in the range of the drone would allow it to visit an additional three locations. How long would it now take the drone to evaluate all solutions?
'''

class tsp():

	def calc_routes(self):
		starting_value = 1
		number_of_routes = 1
		
		while starting_value < self.number_of_locations:
			number_of_routes = number_of_routes * starting_value
			starting_value += 1
		
		return number_of_routes/2

	def proc_time(self):
		return self.calc_routes()/self.routes_per_second_processed

	def time_calculations(self):
		time = self.processing_time
		days = 0
		hours = 0
		mins = 0

		# Calculating Days
		while time > 86400:
			time -= 86400
			days += 1		

		# Calculating Hours
		while time > 3600:
			time -= 3600
			hours += 1

		# Calculating Minutes
		while time > 60:
			time -= 60
			mins += 1

		return (f'{days} day(s), {hours} hour(s), {mins} minute(s), {time} second(s) \n')

	def __init__(self, number_of_locations, routes_per_second_processed):
		self.number_of_locations = number_of_locations
		self.routes_per_second_processed = routes_per_second_processed
		self.total_route_options = self.calc_routes()
		self.processing_time = self.proc_time()

	def __str__(self):
		return f'The total number of route options for {self.number_of_locations} locations is: {self.total_route_options} \nThe processing time required is: {self.time_calculations()}'


def main():
	# Update the line below with your given paramaters tsp(number_of_locations, routes_per_second_processed)
	the_drone = tsp(19, 70000000)

	print(the_drone)

if __name__=='__main__':
	main()
	
