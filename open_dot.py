
import geoplotlib
from geoplotlib.utils import read_csv

from decor import nice

def show_map():

	data = read_csv('data.csv')
	geoplotlib.dot(data)
	geoplotlib.show()




@nice
def main():
	show_map()

if __name__ == '__main__':
	main()