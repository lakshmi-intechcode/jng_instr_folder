
pop_file = "population.csv"

def read_this(filename):
	with open(filename) as entire_txt:
		txt = entire_txt.read()
	return txt


print(read_this(pop_file))


